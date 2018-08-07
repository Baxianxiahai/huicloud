using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.IO;

[StructLayout(LayoutKind.Sequential, Pack = 1)]
public struct IHU_HUITP_L2FRAME_STD_frame_header
{
    public byte start;
    public byte chksum;
    public UInt16 len;     // the length including the size of header
}



[StructLayout(LayoutKind.Sequential, Pack = 1)]
unsafe public struct VCI_CAN_OBJ
{
    public uint ID;
    public uint TimeStamp;        //时间标识
    public byte TimeFlag;         //是否使用时间标识
    public byte SendType;         //发送标志。保留，未用
    public byte RemoteFlag;       //是否是远程帧
    public byte ExternFlag;       //是否是扩展帧
    public byte DataLen;

    public fixed byte Data[8];

    public fixed byte Reserved[3];

}

[StructLayout(LayoutKind.Sequential, Pack = 1)]
public unsafe struct IHU_HUITP_L2FRAME_Desc_s
{
    public UInt32 RxState;
    public fixed byte pRxBuffPtr[256];
    public UInt16 RxBuffSize;
    public UInt16 RxXferCount;
}

[StructLayout(LayoutKind.Sequential, Pack = 1)]
public unsafe struct BOOTCFG
{
    public fixed byte equLable[20];
    public UInt16 hwType;
    public UInt16 hwPemId;
    public UInt16 swRelId;
    public UInt16 swVerId;
    public byte swUpgradeFlag;
    public byte swUpgPollId;
    public byte bootIndex;
    public byte bootAreaMax;
    public fixed byte cipherKey[16];
    
}

namespace fmpt
{

    public partial class Form1 : Form
    {
        VCI_CAN_OBJ[] m_recobj = new VCI_CAN_OBJ[100];
        public IHU_HUITP_L2FRAME_Desc_s frame_desc = new IHU_HUITP_L2FRAME_Desc_s();
        public BOOTCFG bootcfg_value = new BOOTCFG();

        byte[] bootcfg_buf = new byte[Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA];
        //bootcfgRegister:add, length, data_type
        public static field_def EQU_LABLE = new field_def(0x080E0000, 20, 1);
        public static field_def HW_TYPE = new field_def(0x080E0014, 2, 1);
        public static field_def HW_PEM_ID = new field_def(0x080E0016, 2, 1);
        public static field_def SW_REL_ID = new field_def(0x080E0018, 2, 1);
        public static field_def SW_VER_ID = new field_def(0x080E001A, 2, 1);
        public static field_def SW_UPGRADE_FLAG = new field_def(0x080E001C, 1, 1);
        public static field_def SW_UPGRAPOLL_ID = new field_def(0x080E001D, 1, 1);
        public static field_def BOOT_INDEX = new field_def(0x080E001E, 1, 1);
        public static field_def BOOT_AREA_MAX = new field_def(0x080E001F, 1, 1);
        public static field_def CIPHER_KEY = new field_def(0x080E0060, 16, 1);
        public TextBox[] bootCfg_textbox = new TextBox[BOOT_CFG.Length];
        public static field_def[] BOOT_CFG =
        {
            EQU_LABLE,
            HW_TYPE,
            HW_PEM_ID,
            SW_REL_ID,
            SW_VER_ID,
            SW_UPGRADE_FLAG,
            SW_UPGRAPOLL_ID,
            BOOT_INDEX,
            BOOT_AREA_MAX,
            CIPHER_KEY,
        };


        public UInt32 bootcfg_bitmap = 0;
        public byte pending_cmd = 0;
        public process_control pc = new process_control(-1, -1, -1, -1, 0, 0);

        // function state machine, operation will complete accordding the table step by step
        public SByte[,] status_table = new SByte[Constants.MAX_ROW_STATUS, Constants.MAX_COL_STATUS]
        {
            {Constants.READ_BOOTCFG_STATUS, -1, -1, -1, -1, -1, -1, -1, -1, -1}, //load bootcfg
            {Constants.ERASE_BOOTCFG_STATUS, Constants.WRITE_BOOTCFG_STATUS, -1, -1, -1, -1, -1, -1, -1, -1}, //update bootcfg
            {Constants.ERASE_FAC_STATUS, Constants.WRITE_FAC_STATUS, -1, -1, -1, -1, -1, -1, -1, -1},  //fac load
            {Constants.ERASE_APP1_STATUS, Constants.WRITE_APP1_STATUS, -1, -1, -1, -1, -1, -1, -1, -1},  //APP1 load
            {Constants.ERASE_APP2_STATUS, Constants.WRITE_APP2_STATUS, -1, -1, -1, -1, -1, -1, -1, -1},  //APP2 load
            {Constants.UPDATE_FAC_STATUS, Constants.UPDATE_APP1_STATUS, Constants.UPDATE_APP2_STATUS, -1, -1, -1, -1, -1, -1, -1},  //BURN fac/app1/app2 load
            {Constants.UPDATE_BOOTCFG_STATUS, Constants.UPDATE_FAC_STATUS, Constants.UPDATE_APP1_STATUS, Constants.UPDATE_APP2_STATUS, -1, -1, -1, -1, -1, -1},  //BURN bootcfg/fac/app1/app2 load
            {Constants.READ_IMAGE2DISK_STATUS, -1, -1, -1, -1, -1, -1, -1, -1, -1},//save image to disk
            {Constants.ERASE_FLASHBOOTCFG_STATUS, Constants.ERASE_FLASHFAC_STATUS, Constants.ERASE_FLASHAPP1_STATUS, Constants.ERASE_FLASHAPP2_STATUS,
                Constants.WRITE_FLASHBOOTCFG_STATUS, Constants.WRITE_FLASHFAC_STATUS, Constants.WRITE_FLASHAPP1_STATUS, Constants.WRITE_FLASHAPP2_STATUS, -1, -1}, //load image to flash

            {Constants.READ_BOOTCFG_ALL_FIELDS_STATUS, Constants.ERASE_BOOTCFG_STATUS, Constants.WRITE_BOOTCFG_SINGLE_FIELD_STATUS, -1, -1, -1, -1, -1, -1, -1}
            //{-1,-1, -1, -1, -1, -1, -1, -1, -1, -1}
        };

        public TextBox ret_text_box = null;//for save read register textbox

        public Int32 remoteflag = 0;
        public Int32 extflag = 0;
        public string id = "";
        public UInt32 devtype = 0;
        public UInt32 devind = 0;
        public UInt32 canind = 0;
        public UInt32 bopen = 0;
        Byte[] buffertrans = new byte[128];
        public static string equlablestr;
        public static string hwtypestr;
        public static string hwpemidstr;
        public static string swrelidstr;
        public static string swveridstr;
        public static string swupgradeflagstr;
        public static string swupgpollidstr;
        public static string bootindexstr;
        public static string bootareamaxstr;
        public static string cipherkeystr;


        [DllImport("controlcan.dll")]
        static extern UInt32 VCI_Transmit(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd, ref VCI_CAN_OBJ pSend, UInt32 Len);

        [DllImport("controlcan.dll")]
        static extern UInt32 VCI_Receive(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd, ref VCI_CAN_OBJ pReceive, UInt32 Len, Int32 WaitTime);

        public Form1()
        {
            InitializeComponent();
            initialBootCfgTextBox();

        }
        public void initialBootCfgTextBox()
        {
            bootCfg_textbox[0] = textBox_equaLable;
            bootCfg_textbox[1] = textBox_hwType;
            bootCfg_textbox[2] = textBox_hwPemId;
            bootCfg_textbox[3] = textBox_swRelId;
            bootCfg_textbox[4] = textBox_swVerId;
            bootCfg_textbox[5] = textBox_swUpgradeFlag;
            bootCfg_textbox[6] = textBox_swUpgPollId;
            bootCfg_textbox[7] = textBox_bootIndex;
            bootCfg_textbox[8] = textBox_bootAreaMax;
            bootCfg_textbox[9] = textBox_cipherKey;

        }

        /**************************************************************************/
        /* get current ongoing operation
         * 
         * input : operate status  
         * 
         * output : operate index
        **************************************************************************/
        public SByte get_current_op(SByte status_top, SByte status_mid, SByte status_low)
        {
            SByte ret;
            if (status_top == -1)
                return -1;

            ret = status_table[status_top, status_mid];

            if (status_low == -1)
                return ret;
            else //burn 
            {
                if (ret == Constants.UPDATE_BOOTCFG_STATUS)
                {
                    return status_table[Constants.UPDATE_BOOTCFG_TOP_STATUS, status_low];
                }
                else if (ret == Constants.UPDATE_FAC_STATUS)
                {
                    return status_table[Constants.UPDATE_FAC_TOP_STATUS, status_low];
                }
                else if (ret == Constants.UPDATE_APP1_STATUS)
                {
                    return status_table[Constants.UPDATE_APP1_TOP_STATUS, status_low];

                }
                else if (ret == Constants.UPDATE_APP2_STATUS)
                {
                    return status_table[Constants.UPDATE_APP2_TOP_STATUS, status_low];
                }
                else
                {
                    return -1;
                }
            }

        }
        /**************************************************************************/
        /* the real process of different operation
         * 
         * input : operate status  
         * 
         * output : 
        **************************************************************************/
        public unsafe void status_handler(SByte status_top, SByte status_mid, SByte status_low)
        {
            SByte current_operation;

            current_operation = get_current_op(status_top, status_mid, status_low);//status_table[status_top, status_mid];

            listBox_debug.Items.Add("[status] top =0x" + System.Convert.ToString(status_top, 16) + " mid=0x" + System.Convert.ToString(status_mid, 16) + " low=0x" + System.Convert.ToString(status_low, 16));
            listBox_debug.Items.Add("[current_op] cur=0x" + System.Convert.ToString(current_operation, 16));
            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

            if (current_operation == -1)
                return;

            switch (current_operation)
            {
                case Constants.READ_BOOTCFG_ALL_FIELDS_STATUS:
                    {
                        UInt32 read_len = (UInt32)((pc.write_total_len_in_byte + Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA > sizeof(BOOTCFG)) ? (sizeof(BOOTCFG) - pc.write_total_len_in_byte) : Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA);

                        if (sizeof(BOOTCFG) > Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA)
                        {
                            listBox_debug.Items.Add("[ERROR] BOOTCFG LEN TOO LONG!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                            return;
                        }

                        if (pc.write_total_len_in_byte > 0)
                        {
                            UInt32 valid_len = (UInt32)((pc.write_total_len_in_byte == sizeof(BOOTCFG)) ? (sizeof(BOOTCFG) % Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA) : Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA);
                            int size = Marshal.SizeOf(bootcfg_value);
                            IntPtr intptr = Marshal.AllocHGlobal(size);
                            Marshal.StructureToPtr(bootcfg_value, intptr, true);
                            byte* dat = (byte*)intptr.ToPointer();
                            fixed (byte* rx = frame_desc.pRxBuffPtr)
                            {
                                for (int i = 0; i < valid_len; i++)
                                {
                                    dat[i] = rx[i];
                                }

                            }

                        }

                        if (pc.write_total_len_in_byte >= sizeof(BOOTCFG))
                            pc.write_finish = 1;
                        else
                            read_register(Constants.FLASH_ADDRESS_SW_CONTROL_TABLE, read_len, null);


                        pc.write_total_len_in_byte += read_len;

                    }
                    break;
                case Constants.READ_BOOTCFG_STATUS:
                    {
                        read_register(BOOT_CFG[pc.bootcfg_line_num].addr, 128, bootCfg_textbox[pc.bootcfg_line_num]);
                    }
                    break;
                case Constants.WRITE_BOOTCFG_SINGLE_FIELD_STATUS:
                    {
                        int size = Marshal.SizeOf(bootcfg_value);
                        IntPtr intptr = Marshal.AllocHGlobal(size);
                        setSingleFieldAccordingBitMap();

                        Marshal.StructureToPtr(bootcfg_value, intptr, true);
                        UInt32* dat = (UInt32*)intptr.ToPointer();
                        UInt32[] value = new UInt32[Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA / 4];
                        for (int ii = 0; ii < value.Length; ii++)
                        {
                            value[ii] = dat[ii];
                        }
                        write_register(Constants.FLASH_ADDRESS_SW_CONTROL_TABLE, (UInt32)Marshal.SizeOf(bootcfg_value), value);
                    }
                    break;
                case Constants.ERASE_BOOTCFG_STATUS:
                    EraseFlash(Constants.FLASH_SEC11, 1);
                    break;
                case Constants.WRITE_BOOTCFG_STATUS:                
                    {            
                        //LC:here to achieve the write once function

                        Byte[] textBox1buffer = new byte[20];
                        textBox1buffer = System.Text.Encoding.Default.GetBytes(textBox1.Text);

                        Byte[] textBox2buffer = new byte[2];
                        textBox2buffer = System.Text.Encoding.Default.GetBytes(textBox2.Text);

                        Byte[] textBox3buffer = new byte[2];
                        textBox3buffer = System.Text.Encoding.Default.GetBytes(textBox3.Text);
                  
                        Byte[] textBox4buffer = new byte[2];
                        textBox4buffer = System.Text.Encoding.Default.GetBytes(textBox4.Text);
 
                        Byte[] textBox5buffer = new byte[2];
                        textBox5buffer = System.Text.Encoding.Default.GetBytes(textBox5.Text);
                    
                        Byte[] textBox6buffer = new byte[1];
                        textBox6buffer = System.Text.Encoding.Default.GetBytes(textBox6.Text);

                        Byte[] textBox7buffer = new byte[1];
                        textBox7buffer = System.Text.Encoding.Default.GetBytes(textBox7.Text);
        
                        Byte[] textBox8buffer = new byte[1];
                        textBox8buffer = System.Text.Encoding.Default.GetBytes(textBox8.Text);

                        Byte[] textBox9buffer = new byte[1];
                        textBox9buffer = System.Text.Encoding.Default.GetBytes(textBox9.Text);
                  
                        Byte[] textBox10buffer = new byte[16];
                        textBox10buffer = System.Text.Encoding.Default.GetBytes(textBox10.Text);

                        Byte[] lastbuffer = new byte[16];
                        lastbuffer = System.Text.Encoding.Default.GetBytes(textBox10.Text);

                        Byte[] midbuffer = new byte[64];
                        midbuffer = lastbuffer.Concat(lastbuffer).Concat(lastbuffer).Concat(lastbuffer).ToArray();


                        buffertrans = textBox1buffer.Concat(textBox2buffer).Concat(textBox3buffer).Concat(textBox4buffer).Concat(textBox5buffer).Concat(textBox6buffer).Concat(textBox7buffer).Concat(textBox8buffer).Concat(textBox9buffer).Concat(midbuffer).Concat(textBox10buffer).Concat(lastbuffer).ToArray();
                  
                        string buffertransstr;
                        buffertransstr = System.Text.Encoding.Default.GetString(buffertrans);  

                        UInt32[] value = bytestring_to_UInt32(buffertransstr, 128);    //JUST SOLVE THIS ALL WILL BE OK
                   
                        write_register(0x080E0000, 128, value);
                        pc.write_finish = 1;
                        /*
                        string filePath = @textBox_bootcfg_path.Text;
                         // int i = 0;
                         string[] str = File.ReadAllLines(@filePath);
                         while (BOOT_CFG[pc.bootcfg_line_num].valid == 0)
                         {
                             if (pc.bootcfg_line_num == BOOT_CFG.Length - 1)
                                 break;

                             pc.bootcfg_line_num++;
                         }

                         if (BOOT_CFG[pc.bootcfg_line_num].valid == 1)
                         {
                             int equal_idx = str[pc.bootcfg_line_num].IndexOf("=");
                             string sub_str = str[pc.bootcfg_line_num].Substring(equal_idx + 1);

                             if (BOOT_CFG[pc.bootcfg_line_num].len > 4)
                             {
                                 UInt32[] value = bytestring_to_UInt32(sub_str, (UInt16)BOOT_CFG[pc.bootcfg_line_num].len);
                                 write_register(BOOT_CFG[pc.bootcfg_line_num].addr, BOOT_CFG[pc.bootcfg_line_num].len, value);
                             }
                             else
                             {
                                 UInt32[] value = string_to_UInt32(sub_str, (UInt16)BOOT_CFG[pc.bootcfg_line_num].len);
                                 write_register(BOOT_CFG[pc.bootcfg_line_num].addr, BOOT_CFG[pc.bootcfg_line_num].len, value);
                             }
                         }
                         pc.bootcfg_line_num++;
                         if (pc.bootcfg_line_num == BOOT_CFG.Length) //finish
                         
                             pc.write_finish = 1;
                         }*/
                    }
                    break;
                case Constants.ERASE_FLASHBOOTCFG_STATUS:
                    {
                        EraseFlash(Constants.FLASH_SEC11, 1);
                    }
                    break;
                case Constants.ERASE_FLASHFAC_STATUS:
                    {
                        EraseFlash(Constants.FLASH_SEC5, 2);
                    }
                    break;
                case Constants.ERASE_FLASHAPP1_STATUS:
                    {
                        EraseFlash(Constants.FLASH_SEC7, 2);
                    }
                    break;
                case Constants.ERASE_FLASHAPP2_STATUS:
                    {
                        EraseFlash(Constants.FLASH_SEC9, 2);
                    }
                    break;

                case Constants.ERASE_FAC_STATUS:
                    {
                        EraseFlash(Constants.FLASH_SEC5, 2);
                    }
                    break;
                case Constants.ERASE_APP1_STATUS:
                    EraseFlash(Constants.FLASH_SEC7, 2);
                    break;
                case Constants.ERASE_APP2_STATUS:
                    EraseFlash(Constants.FLASH_SEC9, 2);
                    break;
                /*case Constants.UPDATE_FAC_STATUS:
                case Constants.UPDATE_APP1_STATUS:
                case Constants.UPDATE_APP2_STATUS:*/
                default:
                    return;
            }
            /*******************update status**********************/
            switch (pc.status_top)
            {
                case Constants.LOAD_BOOTCFG_TOP_STATUS:
                    {
                        /*if (current_operation < Constants.CIPHER_KEY_STATUS)
                            pc.status_mid++;
                        else  //finish
                        */
                        if (pc.bootcfg_line_num == 0) //finish
                        {

                            pc.status_top = -1;
                            pc.status_mid = -1;
                            pc.status_low = -1;
                            pc.bootcfg_line_num = -1;
                        }
                    }
                    break;
                case Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS:
                    {
                        if ((current_operation < Constants.WRITE_BOOTCFG_SINGLE_FIELD_STATUS) && (pc.write_finish == 1))
                        {
                            pc.status_mid++;
                        }
                        else
                        {
                            pc.status_top = 1;
                            pc.status_mid = 0;
                            pc.status_low = -1;
                            pc.write_total_len_in_byte = 0;
                            pc.write_finish = 0;
                            listBox_debug.Items.Add("[status] BOOTCFG SINGLE FEILD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                        }

                    }
                    break;
                case Constants.UPDATE_BOOTCFG_TOP_STATUS:
                    {
                        if (current_operation < Constants.WRITE_BOOTCFG_STATUS)
                        {
                            pc.status_mid++;
                        }

                        if (pc.write_finish == 1) //(pc.bootcfg_line_num == BOOT_CFG.Length) //finish
                        {
                            pc.status_top = -1;
                            pc.status_mid = -1;
                            pc.status_low = -1;
                            pc.bootcfg_line_num = -1;
                            pc.write_finish = 0;
                            listBox_debug.Items.Add("[status] BOOTCFG LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                        }
                    }
                    break;

                case Constants.LOAD_IMAGE2FLASH_TOP_STATUS:
                    {
                        if (current_operation < Constants.WRITE_FLASHAPP2_STATUS)
                        {
                            if (current_operation < Constants.WRITE_FLASHBOOTCFG_STATUS)
                                pc.status_mid++;
                            else
                            {
                                if (pc.write_finish == 1)
                                {
                                    pc.status_mid++;
                                    pc.write_finish = 0;
                                    pc.write_total_len_in_byte = 0;
                                }

                            }

                        }
                        else if (pc.write_finish == 1)
                        {
                            pc.status_top = -1;
                            pc.status_mid = -1;
                            pc.status_low = -1;
                            pc.write_total_len_in_byte = 0;
                            pc.write_finish = 0;
                            listBox_debug.Items.Add("[status loadimage2flash] LOAD IMAGE2FLASH FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                    }
                    break;

                case Constants.UPDATE_FAC_TOP_STATUS:
                    {
                        if (current_operation < Constants.WRITE_FAC_STATUS)
                        {
                            pc.status_mid++;
                        }
                        if (pc.write_finish == 1)
                        {
                            pc.status_top = -1;
                            pc.status_mid = -1;
                            pc.status_low = -1;
                            pc.write_total_len_in_byte = 0;
                            pc.write_finish = 0;
                            listBox_debug.Items.Add("[status] FAC LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                    }
                    break;

                case Constants.UPDATE_APP1_TOP_STATUS:
                    {
                        if (current_operation < Constants.WRITE_APP1_STATUS)
                        {
                            pc.status_mid++;
                        }
                        if (pc.write_finish == 1)
                        {
                            pc.status_top = -1;
                            pc.status_mid = -1;
                            pc.status_low = -1;
                            pc.write_total_len_in_byte = 0;
                            pc.write_finish = 0;
                            listBox_debug.Items.Add("[status] APP1 LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                    }
                    break;
                case Constants.UPDATE_APP2_TOP_STATUS:
                    {
                        if (current_operation < Constants.WRITE_APP2_STATUS)
                        {
                            pc.status_mid++;
                        }
                        if (pc.write_finish == 1)
                        {
                            pc.status_top = -1;
                            pc.status_mid = -1;
                            pc.status_low = -1;
                            pc.write_total_len_in_byte = 0;
                            pc.write_finish = 0;
                            listBox_debug.Items.Add("[status] APP2 LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                    }
                    break;

                case Constants.BURN_FAC_APP_TOP_STATUS:
                    {
                        if ((current_operation == Constants.WRITE_FAC_STATUS) && (pc.write_finish == 1))
                        {
                            pc.status_mid++;
                            pc.status_low = 0;
                            pc.write_finish = 0;
                            pc.write_total_len_in_byte = 0;
                            listBox_debug.Items.Add("[status BURN] FAC LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                        else if ((current_operation == Constants.WRITE_APP1_STATUS) && (pc.write_finish == 1))
                        {
                            pc.status_mid++;
                            pc.status_low = 0;
                            pc.write_finish = 0;
                            pc.write_total_len_in_byte = 0;
                            listBox_debug.Items.Add("[status BURN] APP1 LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                        else if ((current_operation == Constants.WRITE_APP2_STATUS) && (pc.write_finish == 1))
                        {
                            pc.status_top = -1;
                            pc.status_mid = -1;
                            pc.status_low = -1;
                            pc.write_total_len_in_byte = 0;
                            pc.write_finish = 0;
                            listBox_debug.Items.Add("[status BURN] APP2 LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;


                        }
                        else
                        {
                            if ((current_operation == Constants.ERASE_FAC_STATUS) ||
                                (current_operation == Constants.ERASE_APP1_STATUS) ||
                                (current_operation == Constants.ERASE_APP2_STATUS))
                                pc.status_low++;
                        }
                    }
                    break;
                case Constants.BURN_BOOT_FAC_APP_TOP_STATUS:
                    {
                        if ((current_operation == Constants.WRITE_BOOTCFG_STATUS) && (pc.write_finish == 1))
                        {
                            pc.status_mid++;
                            pc.status_low = 0;
                            pc.write_finish = 0;
                            pc.write_total_len_in_byte = 0;
                            listBox_debug.Items.Add("[status BURN] BOOTCFG LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                        else if ((current_operation == Constants.WRITE_FAC_STATUS) && (pc.write_finish == 1))
                        {
                            pc.status_mid++;
                            pc.status_low = 0;
                            pc.write_finish = 0;
                            pc.write_total_len_in_byte = 0;
                            listBox_debug.Items.Add("[status BURN] FAC LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                        else if ((current_operation == Constants.WRITE_APP1_STATUS) && (pc.write_finish == 1))
                        {
                            pc.status_mid++;
                            pc.status_low = 0;
                            pc.write_finish = 0;
                            pc.write_total_len_in_byte = 0;
                            listBox_debug.Items.Add("[status BURN] APP1 LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                        else if ((current_operation == Constants.WRITE_APP2_STATUS) && (pc.write_finish == 1))
                        {
                            pc.status_top = -1;
                            pc.status_mid = -1;
                            pc.status_low = -1;
                            pc.write_total_len_in_byte = 0;
                            pc.write_finish = 0;
                            listBox_debug.Items.Add("[status BURN] APP2 LOAD UPDATE FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                        }
                        else
                        {
                            if ((current_operation == Constants.ERASE_FAC_STATUS) ||
                                (current_operation == Constants.ERASE_APP1_STATUS) ||
                                (current_operation == Constants.ERASE_APP2_STATUS) ||
                                (current_operation == Constants.ERASE_BOOTCFG_STATUS))
                                pc.status_low++;
                        }
                    }
                    break;
                case Constants.SAVE_IMAGE2DISK_TOP_STATUS:
                    {
                        if (pc.write_finish == 1)
                        {
                            pc.status_top = -1;
                            pc.status_mid = -1;
                            pc.status_low = -1;
                            pc.write_finish = 0;
                            pc.write_total_len_in_byte = 0;
                            listBox_debug.Items.Add("[status save_image] IMAGE SAVE TO DISK FINISH!!!!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                        }

                    }
                    break;
                default:
                    return;

            }
            listBox_debug.Items.Add("[status end] top =0x" + System.Convert.ToString(status_top, 16) + " mid=0x" + System.Convert.ToString(status_mid, 16) + " low=0x" + System.Convert.ToString(status_low, 16));
            //listBox_debug.Items.Add("[current_op] cur=0x" + System.Convert.ToString(current_operation, 16));
            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

            /************************************************/
            /*if (pc.status_top == Constants.LOAD_BOOTCFG_TOP_STATUS)
            {
                if (current_operation < Constants.CIPHER_KEY_STATUS)
                    pc.status_mid++;
                else  //finish
                {
                    pc.status_top = -1;
                    pc.status_mid = -1;
                    //pc.status_low = -1;
                }
            }
            else if (pc.status_top == Constants.UPDATE_BOOTCFG_TOP_STATUS)
            {
                if (current_operation < Constants.WRITE_BOOTCFG_STATUS)
                {
                    pc.status_mid++;
                }

                if (pc.bootcfg_line_num == BOOT_CFG.Length)
                {
                    pc.status_top = -1;
                    pc.status_mid = -1;
                    //pc.status_low = -1;
                }
            }*/



            /* }
             else //burn
             {
                 if (status_low == Constants.BURN_FAC_APP_TOP_STATUS)
                 {
                     if (status_mid == Constants.BURN_FAC_STATUS)
                     {
                         status_handler(status_top, status_mid, -1);
                     }
                 }

             }*/

        }


        /**************************************************************************/
        /* find sec according to the addr
         * 
         * input : regiter address
         * 
         * output : sector index
        **************************************************************************/
        unsafe public byte FindSec(UInt32 addr)
        {
            if ((addr >= Constants.FLASH_START_ADDRESS_SEC0) && (addr < Constants.FLASH_START_ADDRESS_SEC1))
            {
                return Constants.FLASH_SEC0;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC1) && (addr < Constants.FLASH_START_ADDRESS_SEC2))
            {
                return Constants.FLASH_SEC1;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC2) && (addr < Constants.FLASH_START_ADDRESS_SEC3))
            {
                return Constants.FLASH_SEC2;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC3) && (addr < Constants.FLASH_START_ADDRESS_SEC4))
            {
                return Constants.FLASH_SEC3;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC4) && (addr < Constants.FLASH_START_ADDRESS_SEC5))
            {
                return Constants.FLASH_SEC4;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC5) && (addr < Constants.FLASH_START_ADDRESS_SEC6))
            {
                return Constants.FLASH_SEC5;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC6) && (addr < Constants.FLASH_START_ADDRESS_SEC7))
            {
                return Constants.FLASH_SEC6;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC7) && (addr < Constants.FLASH_START_ADDRESS_SEC8))
            {
                return Constants.FLASH_SEC7;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC8) && (addr < Constants.FLASH_START_ADDRESS_SEC9))
            {
                return Constants.FLASH_SEC8;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC9) && (addr < Constants.FLASH_START_ADDRESS_SEC10))
            {
                return Constants.FLASH_SEC9;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC10) && (addr < Constants.FLASH_START_ADDRESS_SEC11))
            {
                return Constants.FLASH_SEC10;
            }
            else if ((addr >= Constants.FLASH_START_ADDRESS_SEC11) && (addr < Constants.FLASH_MAX_ADDRESS))
            {
                return Constants.FLASH_SEC11;
            }
            else
            {
                return 0xFF;
            }
        }
        unsafe public void GetSecInfo(UInt32 addr, UInt32 len, ref byte startSec, ref byte numSec)
        {
            byte endSec = 0;

            startSec = FindSec(addr);
            endSec = FindSec(addr + len - 1);

            if (startSec == 0xFF || endSec == 0xFF)
            {
                numSec = 0xFF;
            }
            else
            {
                numSec = (byte)(endSec - startSec + 1);
            }
        }



      
        //LC: here is the reversal functions
        public static UInt16 ENDIAN_EXG16(UInt16 value)
        {
            return (UInt16)(((value & 0xFF00) >> 8) | ((value & 0x00FF) << 8));
        }

        public static UInt32 ENDIAN_EXG32(UInt32 value)
        {
            return (((value & 0xFF000000) >> 24) | ((value & 0x00FF0000) >> 8) | ((value & 0x0000FF00) << 8) | ((value & 0x000000FF) << 24));
        }

      
        /******/
        public unsafe void read_register(UInt32 addr, UInt32 len, TextBox dest)
        {
            msg_struct_l3iap_flash_raw_command_req snd;
            IHU_HUITP_L2FRAME_STD_frame_header header;

            byte* byData = (byte*)&header;
            byte* byData2 = (byte*)&snd;
            //byte test1 = 0;
            if (pending_cmd != 0)
            {
                listBox_debug.Items.Add("cmd fail because of pending cmd exist! ");
                listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                return;
            }


            snd.msgid = ENDIAN_EXG16(Constants.HUITP_MSGID_sui_flash_raw_cmd_req);

            snd.length = ENDIAN_EXG16((UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) - 4));
            snd.flashRawCommandMode = Constants.IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
            snd.flashRawCommand = Constants.IAP_FLASH_RAW_COMMAND_READ;
            snd.flashAddressToAccess = ENDIAN_EXG32(addr);//System.Convert.ToUInt32(textBox_FlashAddr.Text,16);
            snd.flashValidLengthToAccess = ENDIAN_EXG32(len);//(UInt32)((radioButton_byte.Checked == true) ? 1:(radioButton_short.Checked == true ? 2:4));

            header.start = Constants.IHU_L2PACKET_START_CHAR;
            header.len = (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) + 4);

            header.chksum = (byte)(byData[0] ^ byData[2] ^ byData[3]);
            //send out
            // memset(ctrlMsgBuf, 0, Constants.MAX_WMC_CONTROL_MSG_LEN);

            byte[] ctrlMsgBuf = new byte[256];   //LC :reverse endian needs more space
            for (int i = 0; i < 4; i++)
            {
                fixed (byte* test1 = &ctrlMsgBuf[i])
                {
                    //ctrlMsgBuf[i] = byData[i];
                    *(test1) = byData[i];
                }
            }

            for (int ij = 4; ij < (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) - 4); ij++)  //LC : be careful about the length
            {

                fixed (byte* test1 = &ctrlMsgBuf[ij])
                {
                    //ctrlMsgBuf[ii] = byData2[ii - 4];
                    *(test1) = byData2[ij - 4];
                }
            }

            // fixed (VCI_CAN_OBJ* m_recobj2 = &m_recobj[j])
            //     {
            //         l2packet_rx_bytes(ref frame_desc, &m_recobj2->Data[0], m_recobj[j].DataLen);
            //     }
            listBox_debug.Items.Add("read addr =0x" + System.Convert.ToString(addr, 16)); // LC :show the original data 
            listBox_debug.Items.Add("read len =0x" + System.Convert.ToString(len, 16));
            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
            pending_cmd = snd.flashRawCommand;
            // can_msg_send(header.len);
            ret_text_box = dest;

            can_msg_send(header.len, ref ctrlMsgBuf[0]);

        }

        public unsafe void write_register(UInt32 addr, UInt32 length, UInt32[] value)
        {
            try
            {
                msg_struct_l3iap_flash_raw_command_req snd = new msg_struct_l3iap_flash_raw_command_req();
                IHU_HUITP_L2FRAME_STD_frame_header header = new IHU_HUITP_L2FRAME_STD_frame_header();

                byte[] ctrlMsgBuf = new byte[256];
                byte* byData = (byte*)&header;
                byte* byData2 = (byte*)&snd;

                if (pending_cmd != 0)
                {
                    listBox_debug.Items.Add("cmd fail because of pending cmd exist! ");
                    listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                }

                snd.msgid = ENDIAN_EXG16(Constants.HUITP_MSGID_sui_flash_raw_cmd_req);
                snd.length = ENDIAN_EXG16((UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) - 4));
                snd.flashRawCommandMode = Constants.IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
                snd.flashRawCommand = Constants.IAP_FLASH_RAW_COMMAND_WRITE;
                snd.flashAddressToAccess = ENDIAN_EXG32(addr);// System.Convert.ToUInt32(textBox_FlashAddr.Text, 16);
                snd.flashValidLengthToAccess = ENDIAN_EXG32(length);// (UInt32)((radioButton_byte.Checked == true) ? 1 : (radioButton_short.Checked == true ? 2 : 4));
                /*
                value = System.Convert.ToUInt32(textBox_readorwriteValue.Text, 16);

                snd.data[0] = (byte)(value & 0xFF);
                snd.data[1] = (byte)((value & 0xFF00) >> 8);
                snd.data[2] = (byte)((value & 0xFF0000) >> 16);
                snd.data[3] = (byte)((value & 0xFF000000) >> 24);
                */
                for (int i = 0; i < ((length + 3) / 4); i++)
                {
                    for (int j = 0; j < 4; j++)
                    {
                        snd.data[i * 4 + j] = (byte)((value[i] >> (j * 8)) & 0xFF);
                    }
                }
                header.start = Constants.IHU_L2PACKET_START_CHAR;
                header.len = (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) + 4);
                header.chksum = (byte)(byData[0] ^ byData[2] ^ byData[3]);
                //send out
                // memset(ctrlMsgBuf, 0, Constants.MAX_WMC_CONTROL_MSG_LEN);
                for (int i = 0; i < 4; i++)
                {

                    fixed (byte* test1 = &ctrlMsgBuf[i])
                    {
                        //ctrlMsgBuf[i] = byData[i];
                        *(test1) = byData[i];
                    }
                }
                for (int ii = 4; ii < (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) - 4); ii++)
                {

                    fixed (byte* test1 = &ctrlMsgBuf[ii])
                    {
                        //ctrlMsgBuf[ii] = byData2[ii - 4];
                        *(test1) = byData2[ii - 4];
                    }
                }
                listBox_debug.Items.Add("write addr =0x" + System.Convert.ToString(snd.flashAddressToAccess, 16));
                listBox_debug.Items.Add("write len =0x" + System.Convert.ToString(snd.flashValidLengthToAccess, 16));
                listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                pending_cmd = snd.flashRawCommand;
                can_msg_send(header.len, ref ctrlMsgBuf[0]);
            }
            catch (Exception ex)
            {
                textBox_equaLable.Text = ex.ToString();
            }
        }

        public static void Delay(int milliSecond)
        {
            int start = Environment.TickCount;
            while (Math.Abs(Environment.TickCount - start) < milliSecond)
            {
                Application.DoEvents();
            }
        }

        public unsafe void can_msg_send(UInt16 msg_len, ref byte data)
        {
          try
          { 
            VCI_CAN_OBJ sendobj = new VCI_CAN_OBJ();
            int jj = 0;

            //ctrlMsgBuf = new byte[256];
            for (int ii = 0; ii < msg_len; ii += 8)
            {
                

                    //sendobj.Init();
                    sendobj.RemoteFlag = (byte)remoteflag;//setup.comboBox_FrameFormat.SelectedIndex;
                    sendobj.ExternFlag = (byte)extflag;//setup.comboBox_FrameType.SelectedIndex; //0x01;
                                                       //listBox_debug.Items.Add("ID=" + id); //0x00100001

                    sendobj.ID = System.Convert.ToUInt32("0x" + id/*setup.textBox_ID.Text*/, 16);// 0x00100001;//0x01;


                    //listBox_debug.Items.Add("sendobj.ID" + sendobj.ID); //1048577
                    listBox_debug.Items.Add("ii=" + ii);
                    if (ii + 8 > msg_len)
                        jj = (msg_len % 8);
                    else
                        jj = 8;

                    sendobj.DataLen = System.Convert.ToByte(jj);
                    for (int iii = 0; iii < jj; iii++)
                    {
                        fixed (byte* test2 = &data/*&ctrlMsgBuf[0]*/)
                        {
                            //sendobj.Data[iii] = ctrlMsgBuf[iii + ii];
                            sendobj.Data[iii] = *(test2 + iii + ii);
                            listBox_debug.Items.Add("data=" + sendobj.Data[iii].ToString("X2"));
                            //Application.DoEvents();
                        }
                    }

                    if (VCI_Transmit(devtype, devind, canind/*setup.m_devtype, setup.m_devind, setup.m_canind*/, ref sendobj, 1) == 0)
                    {
                        MessageBox.Show("fail", "error",
                                MessageBoxButtons.OK, MessageBoxIcon.Exclamation);

                    }
                    Delay(1);  //LC : puls delay solve the no respone 
               


            }
            listBox_debug.Items.Add("send remote =0x" + System.Convert.ToString(sendobj.RemoteFlag, 16));
            listBox_debug.Items.Add("send ext =0x" + System.Convert.ToString(sendobj.ExternFlag, 16));
            listBox_debug.Items.Add("send id =0x" + System.Convert.ToString(sendobj.ID, 16));
            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
          }
              catch (Exception ex)
            {
                throw ex;
            }
    }


        public void open_browser(TextBox desc)
        {
            OpenFileDialog dialog = new OpenFileDialog();
            dialog.Multiselect = false;//该值确定是否可以选择多个文件
            dialog.Title = "请选择文件夹";
            dialog.Filter = "所有文件(*.*)|*.*";
            if (dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                string file = dialog.FileName;
                desc.Text = file;
            }
        }
        /*************/
        unsafe private void UnLockFlash()
        {
            msg_struct_l3iap_flash_raw_command_req snd;
            IHU_HUITP_L2FRAME_STD_frame_header* header;

            byte[] ctrlMsgBuf = new byte[256];
            /* fixed (IHU_HUITP_L2FRAME_STD_frame_header* header1 = &ctrlMsgBuf[0])
             {
                 header = header1;
             }*/
            fixed (byte* by = &ctrlMsgBuf[0])
            {
                header = (IHU_HUITP_L2FRAME_STD_frame_header*)by;
            }

            //header = (IHU_HUITP_L2FRAME_STD_frame_header*)(ctrlMsgBuf);

            byte* byData = (byte*)header;
            byte* byData2 = (byte*)&snd;
            snd.msgid = Constants.HUITP_MSGID_sui_flash_raw_cmd_req;
            snd.length = (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) - 4);
            snd.flashRawCommandMode = Constants.IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
            snd.flashRawCommand = Constants.IAP_FLASH_RAW_COMMAND_FLASH_UNLOCK;

            header->start = Constants.IHU_L2PACKET_START_CHAR;
            header->len = (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) + 4);
            header->chksum = (byte)(byData[0] ^ byData[2] ^ byData[3]);
            //send out
            // memset(ctrlMsgBuf, 0, Constants.MAX_WMC_CONTROL_MSG_LEN);
            for (int ii = 4; ii < snd.length; ii++)
            {
                byData[ii] = byData2[ii - 4];
            }
            listBox_debug.Items.Add("unlock flash ");
            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

            //can_msg_send(header->len);

            can_msg_send(header->len, ref ctrlMsgBuf[0]);
        }

        unsafe private void LockFlash()
        {
            msg_struct_l3iap_flash_raw_command_req snd;
            IHU_HUITP_L2FRAME_STD_frame_header* header;

            byte[] ctrlMsgBuf = new byte[256];
            /* fixed (IHU_HUITP_L2FRAME_STD_frame_header* header1 = &ctrlMsgBuf[0])
             {
                 header = header1;
             }*/
            fixed (byte* by = &ctrlMsgBuf[0])
            {
                header = (IHU_HUITP_L2FRAME_STD_frame_header*)by;
            }

            //header = (IHU_HUITP_L2FRAME_STD_frame_header*)(ctrlMsgBuf);

            byte* byData = (byte*)header;
            byte* byData2 = (byte*)&snd;
            snd.msgid = ENDIAN_EXG16(Constants.HUITP_MSGID_sui_flash_raw_cmd_req);
            snd.length = ENDIAN_EXG16((UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) - 4));
            snd.flashRawCommandMode = Constants.IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
            snd.flashRawCommand = Constants.IAP_FLASH_RAW_COMMAND_FLASH_LOCK;

            header->start = Constants.IHU_L2PACKET_START_CHAR;
            header->len = (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) + 4);
            header->chksum = (byte)(byData[0] ^ byData[2] ^ byData[3]);
            //send out
            // memset(ctrlMsgBuf, 0, Constants.MAX_WMC_CONTROL_MSG_LEN);
            for (int ii = 4; ii < (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) - 4); ii++)
            {
                byData[ii] = byData2[ii - 4];
            }
            listBox_debug.Items.Add("lock flash ");
            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

            //can_msg_send(header->len);

            can_msg_send(header->len, ref ctrlMsgBuf[0]);
        }

        unsafe private void EraseFlash(byte startSec, byte numSec)
        {
            msg_struct_l3iap_flash_raw_command_req snd;
            IHU_HUITP_L2FRAME_STD_frame_header* header;

            byte[] ctrlMsgBuf = new byte[256];
            /* fixed (IHU_HUITP_L2FRAME_STD_frame_header* header1 = &ctrlMsgBuf[0])
             {
                 header = header1;
             }*/
            fixed (byte* by = &ctrlMsgBuf[0])
            {
                header = (IHU_HUITP_L2FRAME_STD_frame_header*)by;
            }

            //header = (IHU_HUITP_L2FRAME_STD_frame_header*)(ctrlMsgBuf);

            byte* byData = (byte*)header;
            byte* byData2 = (byte*)&snd;
            snd.msgid = ENDIAN_EXG16(Constants.HUITP_MSGID_sui_flash_raw_cmd_req);
            snd.length = ENDIAN_EXG16((UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) - 4));
            snd.flashRawCommandMode = Constants.IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
            snd.flashRawCommand = Constants.IAP_FLASH_RAW_COMMAND_SECTOR_ERASE;
            snd.flashSectorIdToErase = startSec;
            snd.flashSectorNumberToErase = numSec;

            header->start = Constants.IHU_L2PACKET_START_CHAR;
            header->len = (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) + 4);
            header->chksum = (byte)(byData[0] ^ byData[2] ^ byData[3]);
            //send out
            // memset(ctrlMsgBuf, 0, Constants.MAX_WMC_CONTROL_MSG_LEN);
            for (int ii = 4; ii < (UInt16)(sizeof(msg_struct_l3iap_flash_raw_command_req) - 4); ii++)
            {
                byData[ii] = byData2[ii - 4];
            }
            listBox_debug.Items.Add("erase flash start sec = 0x" + System.Convert.ToString(startSec, 16));
            listBox_debug.Items.Add("erase flash sec num = 0x" + System.Convert.ToString(numSec, 16));
            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

            //can_msg_send(header->len);
            pending_cmd = snd.flashRawCommand;
            can_msg_send(header->len, ref ctrlMsgBuf[0]);
        }


        private void SetUp_Click(object sender, EventArgs e)
        {
            //Form2 
            Form2 setup = new Form2();
            setup.Owner = this;
            setup.Show();
            button_loadBootCfg.Enabled = true;
        }

        unsafe private void timer_rec_Tick(object sender, EventArgs e)
        {
            try
            {
                UInt32 res = new UInt32();
                //UInt32 iap_len = new UInt32();

                res = VCI_Receive(devtype, devind, canind/*setup.m_devtype, setup.m_devind, setup.m_canind*/, ref m_recobj[0], 1000, 100);

                if (res >= 1000)
                    return;
                if (res > 0)
                {
                    listBox_debug.Items.Add("rcv pkt num = 0x" + System.Convert.ToString(res, 16));
                    listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                    timer_rec.Enabled = false;
                }
                for (UInt32 j = 0; j < res; j++)
                {

                    fixed (VCI_CAN_OBJ* m_recobj2 = &m_recobj[j])
                    {

                        listBox_debug.Items.Add("rcv data = 0x" + System.Convert.ToString(m_recobj2->Data[7], 16)
                            + System.Convert.ToString(m_recobj2->Data[6], 16)
                            + System.Convert.ToString(m_recobj2->Data[5], 16)
                            + System.Convert.ToString(m_recobj2->Data[4], 16) + "   "
                            + System.Convert.ToString(m_recobj2->Data[3], 16)
                            + System.Convert.ToString(m_recobj2->Data[2], 16)
                            + System.Convert.ToString(m_recobj2->Data[1], 16)
                            + System.Convert.ToString(m_recobj2->Data[0], 16));
                        listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                        l2packet_rx_bytes(ref frame_desc, &m_recobj2->Data[0], m_recobj[j].DataLen);

                    }
                }
                timer_rec.Enabled = true;
            }
            catch (Exception ex)
            {
                textBox_equaLable.Text = ex.ToString();
            }
        }

        public unsafe void l2packet_rx_bytes(ref IHU_HUITP_L2FRAME_Desc_s pdesc, byte* data, byte data_size)
        {
            UInt32 i = 0;
            //IHU_HUITP_L2FRAME_STD_frame_header *pMsgHeader;
            //listBox_debug.Items.Add("point test A");
            fixed (byte* pMsgHeader1 = pdesc.pRxBuffPtr)
            {
                IHU_HUITP_L2FRAME_STD_frame_header* pMsgHeader = (IHU_HUITP_L2FRAME_STD_frame_header*)pMsgHeader1;
                for (i = 0; i < data_size; i++)
                {
                    /* save one byte one time */
                    pMsgHeader1[pdesc.RxXferCount] = data[i];
                    pdesc.RxXferCount++;

                    switch (pdesc.RxState)
                    {
                        case Constants.IHU_L2PACKET_RX_STATE_START:
                            if (pMsgHeader->start != Constants.IHU_L2PACKET_START_CHAR)
                            {
                                // not synchonrized, reset the RxXferCount
                                pdesc.RxXferCount = 0;
                                //  listBox_debug.Items.Add("point test B");
                            }
                            else
                                pdesc.RxState = Constants.IHU_L2PACKET_RX_STATE_HEADER;
                            // listBox_debug.Items.Add("point test C");
                            break;

                        case Constants.IHU_L2PACKET_RX_STATE_HEADER:
                            if (pdesc.RxXferCount >= sizeof(IHU_HUITP_L2FRAME_STD_frame_header))
                            {
                                /*if(l2packet_gen_chksum(pMsgHeader) != pMsgHeader->chksum)
                                {
                                    pdesc->RxXferCount = 0;
                                    pdesc->RxState = IHU_L2PACKET_RX_STATE_START;
                                }
                                else*/
                                //listBox_debug.Items.Add("point test D");
                                {
                                    pdesc.RxState = Constants.IHU_L2PACKET_RX_STATE_BODY;
                                    // listBox_debug.Items.Add("point test E");
                                }
                            }
                            break;

                        case Constants.IHU_L2PACKET_RX_STATE_BODY:
                            if (pdesc.RxXferCount >= pMsgHeader->len)
                            {
                                // call user's callback after the receive is complete
                                /*if(pdesc->app_rx_callback)
                                    pdesc->app_rx_callback(pdesc);*/
                                if (*((UInt16*)(&pMsgHeader1[4])) == Constants.HUITP_MSGID_sui_inventory_report)  //inv rep formal is 0x0032
                                {
                                    /*
                                    if (listBox_Info.Items.Count > 200000) { listBox_Info.Items.Clear(); }
                                    listBox_Info.Items.Add("iap_sw_inventory_report rx success!!!");
                                    listBox_Info.SelectedIndex = listBox_Info.Items.Count - 1;
                                    send_iap_sw_inventory_confirm();*/
                                    //listBox_debug.Items.Add("point test F");
                                }
                                else if (*((UInt16*)(&pMsgHeader1[4])) == Constants.HUITP_MSGID_sui_sw_package_report) //pac req former is 0x0034
                                {
                                    /*if (listBox_Info.Items.Count > 200000) { listBox_Info.Items.Clear(); }

                                    info.segIdx = *((UInt16 *)(&pdesc.pRxBuffPtr[13]));//*((UInt32 *)(&pdesc.pRxBuffPtr[20]));
                                    info.segTotal= *((UInt16 *)(&pdesc.pRxBuffPtr[15]));
                                    info.segSplitLen = *((UInt16 *)(&pdesc.pRxBuffPtr[17]));
                                    listBox_Info.Items.Add("iap_sw_package_report rx success!!!");
                                    listBox_Info.Items.Add(System.Convert.ToString(info.segIdx, 16));
                                    listBox_Info.SelectedIndex = listBox_Info.Items.Count - 1;

                                    send_iap_sw_package_confirm();*/
                                    //listBox_debug.Items.Add("point test G");
                                }
                                else if (*((UInt16*)(&pMsgHeader1[4])) == ENDIAN_EXG16(Constants.HUITP_MSGID_sui_flash_raw_cmd_rsp))  //LC: endian change 
                                {
                                    msg_struct_l3iap_flash_raw_command_resp* rcv;
                                    rcv = (msg_struct_l3iap_flash_raw_command_resp*)(&pMsgHeader1[4]);
                                    listBox_debug.Items.Add("iap_flash_raw_cmd_resp rx success!!!");
                                    // listBox_debug.Items.Add("point test H");
                                    listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                                    //  listBox_debug.Items.Add("point test I");
                                    parseResFromLowerLayer(rcv);
                                    // listBox_debug.Items.Add("point test J");

                                }

                                pdesc.RxState = Constants.IHU_L2PACKET_RX_STATE_START;
                                pdesc.RxXferCount = 0;
                            }

                            if (pdesc.RxXferCount >= pdesc.RxBuffSize)
                            {
                                pdesc.RxXferCount = 0;
                                pdesc.RxState = Constants.IHU_L2PACKET_RX_STATE_START;
                            }
                            break;

                        default:
                            pdesc.RxXferCount = 0;
                            pdesc.RxState = Constants.IHU_L2PACKET_RX_STATE_START;
                            break;
                    }
                }
            }
        }
        public unsafe void parseResFromLowerLayer(msg_struct_l3iap_flash_raw_command_resp* rcv)
        {
            if (rcv->flashRawCommandResp == Constants.IAP_FLASH_RAW_COMMAND_RESPONSE_OK)
            {
                switch (pending_cmd)
                {
                    case Constants.IAP_FLASH_RAW_COMMAND_SECTOR_ERASE:
                        {
                            listBox_debug.Items.Add("ERASE OK!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                        }
                        break;

                    case Constants.IAP_FLASH_RAW_COMMAND_FLASH_LOCK:
                        {

                        }
                        break;

                    case Constants.IAP_FLASH_RAW_COMMAND_FLASH_UNLOCK:
                        {

                        }
                        break;


                    case Constants.IAP_FLASH_RAW_COMMAND_WRITE:
                        {
                            listBox_debug.Items.Add("set value = OK!");
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;
                        }
                        break;

                    case Constants.IAP_FLASH_RAW_COMMAND_READ:
                        {

                            String str = "";
                            Byte[] buffer = new byte[128];
                            UInt32 ValidLength_flip = rcv->flashValidLengthToAccess;
                            UInt32 ValidLength = ENDIAN_EXG32(ValidLength_flip);



                            if (ValidLength > Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA)
                            {
                                //IHU_ERROR_PRINT_CANVELA("L3IAP: access length too long, not support!\n");
                                //return IHU_FAILURE;
                            }

                            //ihu_iap_read_flash(rcv.flashAddressToAccess, (uint16_t *)&snd.data[0], rcv.flashValidLengthToAccess);
                            //listBox_debug.Items.Add("POINT BREAK");
                            listBox_debug.Items.Add("rcv value = 0x" + System.Convert.ToString(rcv->data[0], 16) + " 0x" + System.Convert.ToString(rcv->data[1], 16)
                            + " 0x" + System.Convert.ToString(rcv->data[2], 16) + " 0x" + System.Convert.ToString(rcv->data[3], 16));
                            listBox_debug.SelectedIndex = listBox_debug.Items.Count - 1;

                            if (ValidLength == 1)
                            {
                                str += ("0x" + System.Convert.ToString(rcv->data[0], 16));

                            }
                            else if (ValidLength == 2)
                            {
                                str += ("0x" + System.Convert.ToString(rcv->data[1], 16) + System.Convert.ToString(rcv->data[0], 16));

                            }
                            else if (ValidLength == 4)
                            {
                                str += ("0x" + System.Convert.ToString(rcv->data[3], 16) + System.Convert.ToString(rcv->data[2], 16) + System.Convert.ToString(rcv->data[1], 16) + System.Convert.ToString(rcv->data[0], 16));

                            }
                            else
                            {

                                for (int i = 0; i < ValidLength; i++)       //LC: this cycle influence the program
                                {
                                    buffer[i] += rcv->data[i];
                                    listBox_debug.Items.Add("buffer=" + buffer[i]);

                                    /*
                                     * 
                                   str += ("0x" + System.Convert.ToString(rcv->data[i], 16 ));
                                   str += " "; */

                                }
                                for (int i = 0; i < ValidLength; i++)
                                {
                          
                                    buffertrans[i] = buffer[i];
                                    listBox_debug.Items.Add("buffertrans=" + buffertrans[i]);
                                }
                            }
                            // listBox_debug.Items.Add("POINT BREAK 1");
                            //textBox_readorwriteValue.Text = str;
                            
                            
                            if (ret_text_box != null)
                            {
                                //LC:here is the function for read once and display in the textbox
                                Byte[] equlablebuf = new byte[20];
                                equlablebuf = buffer.Skip(0).Take(20).ToArray();
                                for (int i = 0; i < 20; i++)
                                {
                                    equlablestr += ("0x" + System.Convert.ToString(equlablebuf[i], 16));
                                    equlablestr += " ";
                                }

                                Byte[] hwtypebuf = new byte[2];
                                hwtypebuf = buffer.Skip(20).Take(2).ToArray();
                               // Array.Reverse(hwtypebuf);
                                for (int i = 0; i < 2; i++)
                                {
                                    hwtypestr += ("0x" + System.Convert.ToString(hwtypebuf[i], 16));
                                    hwtypestr += " ";
                                }


                                Byte[] hwpemidbuf = new byte[2];
                                hwpemidbuf = buffer.Skip(22).Take(2).ToArray();
                                //Array.Reverse(hwpemidbuf);
                                for (int i = 0; i < 2; i++)
                                {
                                    hwpemidstr += ("0x" + System.Convert.ToString(hwpemidbuf[i], 16));
                                    hwpemidstr += " ";
                                }

                                Byte[] swrelidbuf = new byte[2];
                                swrelidbuf = buffer.Skip(24).Take(2).ToArray();
                                //Array.Reverse(swrelidbuf);
                                for (int i = 0; i < 2; i++)
                                {
                                    swrelidstr += ("0x" + System.Convert.ToString(swrelidbuf[i], 16));
                                    swrelidstr += " ";
                                }

                                Byte[] swveridbuf = new byte[2];
                                swveridbuf = buffer.Skip(26).Take(2).ToArray();
                               // Array.Reverse(swveridbuf);
                                for (int i = 0; i < 2; i++)
                                {
                                    swveridstr += ("0x" + System.Convert.ToString(swveridbuf[i], 16));
                                    swveridstr += " ";
                                }

                                Byte[] swupgradeflagbuf = new byte[1];
                                swupgradeflagbuf = buffer.Skip(28).Take(1).ToArray();
                                for (int i = 0; i < 1; i++)
                                {
                                    swupgradeflagstr += ("0x" + System.Convert.ToString(swupgradeflagbuf[i], 16));
                                    swupgradeflagstr += " ";
                                }


                                Byte[] swupgpollidbuf = new byte[1];
                                swupgpollidbuf = buffer.Skip(29).Take(1).ToArray();
                                for (int i = 0; i < 1; i++)
                                {
                                    swupgpollidstr += ("0x" + System.Convert.ToString(swupgpollidbuf[i], 16));
                                    swupgpollidstr += " ";
                                }

                                Byte[] bootindexbuf = new byte[1];
                                bootindexbuf = buffer.Skip(30).Take(1).ToArray();
                                for (int i = 0; i < 1; i++)
                                {
                                    bootindexstr += ("0x" + System.Convert.ToString(bootindexbuf[i], 16));
                                    bootindexstr += " ";
                                }

                                Byte[] bootareamaxbuf = new byte[1];
                                bootareamaxbuf = buffer.Skip(31).Take(1).ToArray();
                                for (int i = 0; i < 1; i++)
                                {
                                    bootareamaxstr += ("0x" + System.Convert.ToString(bootareamaxbuf[i], 16));
                                    bootareamaxstr += " ";
                                }


                                Byte[] cipherkeybuf = new byte[16];
                                cipherkeybuf = buffer.Skip(96).Take(16).ToArray();
                                for (int i = 0; i < 16; i++)
                                {
                                    cipherkeystr += ("0x" + System.Convert.ToString(cipherkeybuf[i], 16));
                                    cipherkeystr += " ";
                                }
                               
                                textBox_equaLable.Text = equlablestr;
                                textBox_hwType.Text = hwtypestr;
                                textBox_hwPemId.Text = hwpemidstr;
                                textBox_swRelId.Text = swrelidstr;
                                textBox_swVerId.Text = swveridstr;
                                textBox_swUpgradeFlag.Text = swupgradeflagstr;
                                textBox_swUpgPollId.Text = swupgpollidstr;
                                textBox_bootIndex.Text = bootindexstr;
                                textBox_bootAreaMax.Text = bootareamaxstr;
                                textBox_cipherKey.Text = cipherkeystr;
                                //LC: here used to clear the buffer to solve the display bug
                                ret_text_box = null;
                                equlablestr = null;
                                hwtypestr = null;
                                hwpemidstr = null;
                                swrelidstr = null;
                                swveridstr = null;
                                swupgradeflagstr = null;
                                swupgpollidstr = null;
                                bootindexstr = null;
                                bootareamaxstr = null;
                                cipherkeystr = null;
                            }
                            else
                            {

                            }
                        }
                        break;

                    default:
                        //IHU_ERROR_PRINT_CANVELA("L3IAP: Receive unsupported command!\n");
                        //return IHU_FAILURE;
                        break;
                }
                //listBox_debug.Items.Add("END POINT");
                pending_cmd = 0;

                status_handler(pc.status_top, pc.status_mid, pc.status_low);

                //String[] strs = new String[] { "equLable=","hwType=","hwPemId=","swRelId=","swVerId=","swUpgradeFlag=","swUpgPollId=","bootIndex=","bootAreaMax=","facLoadAddr=","facLoadSwRel=","facLoadSwVer=","facLoadCheckSum=","facLoadValid=","facLoadLen=","bootLoad1Addr=","bootLoad1RelId=","bootLoad1VerId=","bootLoad1CheckSum=","bootLoad1Valid=","bootLoad1Len=","bootLoad2Addr=","bootLoad2RelId=","bootLoad2VerId=","bootLoad2CheckSum=","bootLoad2Valid=","bootLoad2Len=", "bootLoad3Addr=0x1111\r\nbootLoad3RelId=0x1111\r\nbootLoad3VerId=0x1111\r\nbootLoad3CheckSum=0x1111\r\nbootLoad3Valid=0x1111\r\nbootLoad3Len=0x1111\r\ncipherKey=","rsv="};

                // j++;

            }

        }

     

        #region BootCfg_Group

        public unsafe void setSingleFieldAccordingBitMap()
        {
            switch (bootcfg_bitmap)
            {
                case Constants.bootcfg_equlabel:
                    {
                        string str = @textBox_equaLable.Text;
                        byte[] val = string_to_byte(str, (UInt16)EQU_LABLE.len);

                        fixed (byte* tmp = bootcfg_value.equLable)
                        {
                            for (int ii = 0; ii < EQU_LABLE.len; ii++)
                                tmp[ii] = val[ii];
                        }
                    }
                    break;
                case Constants.bootcfg_hw_type:
                    {
                        string str = @textBox_hwType.Text;
                        UInt16 len = (UInt16)(HW_TYPE.len / sizeof(UInt16));
                        UInt16[] val = string_to_UInt16(str, len);

                        bootcfg_value.hwType = val[0];
                    }
                    break;
                case Constants.bootcfg_hw_pem_id:
                    {
                        string str = @textBox_hwPemId.Text;
                        UInt16 len = (UInt16)(HW_PEM_ID.len / sizeof(UInt16));
                        UInt16[] val = string_to_UInt16(str, len);

                        bootcfg_value.hwPemId = val[0];
                    }
                    break;
                case Constants.bootcfg_sw_rel_id:
                    {
                        string str = @textBox_swRelId.Text;
                        UInt16 len = (UInt16)(SW_REL_ID.len / sizeof(UInt16));
                        UInt16[] val = string_to_UInt16(str, len);

                        bootcfg_value.swRelId = val[0];
                    }
                    break;
                case Constants.bootcfg_sw_ver_id:
                    {
                        string str = @textBox_swVerId.Text;
                        UInt16 len = (UInt16)(SW_VER_ID.len / sizeof(UInt16));
                        UInt16[] val = string_to_UInt16(str, len);

                        bootcfg_value.swVerId = val[0];
                    }
                    break;
                case Constants.bootcfg_sw_upgrade_flag:
                    {
                        string str = @textBox_swUpgradeFlag.Text;
                        UInt16 len = (UInt16)(SW_UPGRADE_FLAG.len / sizeof(byte));
                        byte[] val = string_to_byte(str, len);

                        bootcfg_value.swUpgradeFlag = val[0];
                    }
                    break;
                case Constants.bootcfg_sw_upgrapoll_id:
                    {
                        string str = @textBox_swUpgPollId.Text;
                        UInt16 len = (UInt16)(SW_UPGRAPOLL_ID.len / sizeof(byte));
                        byte[] val = string_to_byte(str, len);

                        bootcfg_value.swUpgPollId = val[0];
                    }
                    break;
                case Constants.bootcfg_boot_index:
                    {
                        string str = @textBox_bootIndex.Text;
                        UInt16 len = (UInt16)(BOOT_INDEX.len / sizeof(byte));
                        byte[] val = string_to_byte(str, len);

                        bootcfg_value.bootIndex = val[0];
                    }
                    break;
                case Constants.bootcfg_boot_area_max:
                    {
                        string str = @textBox_bootAreaMax.Text;
                        UInt16 len = (UInt16)(BOOT_AREA_MAX.len / sizeof(byte));
                        byte[] val = string_to_byte(str, len);

                        bootcfg_value.bootAreaMax = val[0];
                    }
                    break;
                case Constants.bootcfg_cipher_key:
                    {
                        string str = @textBox_cipherKey.Text;
                        UInt16 len = (UInt16)(CIPHER_KEY.len / sizeof(byte));
                        byte[] val = string_to_byte(str, len);
                        fixed (byte* tmp = bootcfg_value.cipherKey)
                        {
                            for (int ii = 0; ii < len; ii++)
                                tmp[ii] = val[ii];
                        }
                    }
                    break;
                default:
                    break;

            }


            bootcfg_bitmap = 0;
        }

        private void button_equaLable_read_Click(object sender, EventArgs e)
        {

            read_register(EQU_LABLE.addr, EQU_LABLE.len, textBox_equaLable);

        }

        private void button_equaLable_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_equlabel;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }

        private void button_hwType_read_Click(object sender, EventArgs e)
        {
            read_register(HW_TYPE.addr, HW_TYPE.len, textBox_hwType);

        }

        private void button_hwType_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_hw_type;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }

        private void button_hwPemId_read_Click(object sender, EventArgs e)
        {
            read_register(HW_PEM_ID.addr, HW_PEM_ID.len, textBox_hwPemId);
        }

        private void button_hwPemId_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_hw_pem_id;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }

        private void button_swRelId_read_Click(object sender, EventArgs e)
        {
            read_register(SW_REL_ID.addr, SW_REL_ID.len, textBox_swRelId);
        }

        private void button_swRelId_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_sw_rel_id;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }

        private void button_swVerId_read_Click(object sender, EventArgs e)
        {
            read_register(SW_VER_ID.addr, SW_VER_ID.len, textBox_swVerId);
        }

        private void button_swVerId_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_sw_ver_id;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }

        private void button_swUpgradeFlag_read_Click(object sender, EventArgs e)
        {
            read_register(SW_UPGRADE_FLAG.addr, SW_UPGRADE_FLAG.len, textBox_swUpgradeFlag);
        }

        private void button_swUpgradeFlag_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_sw_upgrade_flag;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }

        private void button_swUpgPollId_read_Click(object sender, EventArgs e)
        {
            read_register(SW_UPGRAPOLL_ID.addr, SW_UPGRAPOLL_ID.len, textBox_swUpgPollId);
        }

        private void button_swUpgPollId_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_sw_upgrapoll_id;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }

        private void button_bootIndex_read_Click(object sender, EventArgs e)
        {
            read_register(BOOT_INDEX.addr, BOOT_INDEX.len, textBox_bootIndex);
        }

        private void button_bootIndex_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_boot_index;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }

        private void button_bootAreaMax_read_Click(object sender, EventArgs e)
        {
            read_register(BOOT_AREA_MAX.addr, BOOT_AREA_MAX.len, textBox_bootAreaMax);
        }

        private void button_bootAreaMax_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_boot_area_max;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }

        private void button_cipherKey_read_Click(object sender, EventArgs e)
        {
            read_register(CIPHER_KEY.addr, CIPHER_KEY.len, textBox_cipherKey);
        }

        private void button_cipherKey_write_Click(object sender, EventArgs e)
        {
            bootcfg_bitmap = Constants.bootcfg_cipher_key;
            pc.status_top = Constants.UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;

            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }
     /*   private void button_bootcfg_browser_Click(object sender, EventArgs e)
        {
            //LC:here to create file 
            string path = "C:\\bootcfg.txt";//file path
            FileStream fs = new FileStream(path, FileMode.Create);
            StreamWriter sw = new StreamWriter(fs);
            sw.WriteLine("equaLable=" + textBox1.Text);
            sw.WriteLine("hwType=" + textBox2.Text);
            sw.WriteLine("hwPemId=" + textBox3.Text);
            sw.WriteLine("swRelId=" + textBox4.Text);
            sw.WriteLine("swVerId=" + textBox5.Text);
            sw.WriteLine("swUpgradeFlag=" + textBox6.Text);
            sw.WriteLine("swUpgPollId=" + textBox7.Text);
            sw.WriteLine("bootIndex=" + textBox8.Text);
            sw.WriteLine("bootAreaMax=" + textBox9.Text);
            sw.WriteLine("cipherKey=" + textBox10.Text);
            sw.Close();
            fs.Close();
            open_browser(textBox_bootcfg_path);
        }*/
        private void button_update_bootcfg_Click(object sender, EventArgs e)
        {
           /*  UInt32[] value = new UInt32[10];
             string filePath = @textBox_bootcfg_path.Text;
             int i = 0;
             using (StreamReader sr = new StreamReader(filePath))
             {
                 //一行行读取直至为NULL
                 string strLine = string.Empty;
                 while (strLine != null)
                 {
                     strLine = sr.ReadLine();
                     //找出当前行里所有的数字
                     string result = System.Text.RegularExpressions.Regex.Replace(strLine, @"[^0-9]+", "");
                     value[i++] = System.Convert.ToUInt32(result);
                 }
             }*/
       
            pc.status_top = Constants.UPDATE_BOOTCFG_TOP_STATUS;
            pc.status_mid = 0;
            pc.status_low = -1;
            pc.bootcfg_line_num = 0;
            pc.write_finish = 0;
            status_handler(pc.status_top, pc.status_mid, pc.status_low);

          //  write_register(EQU_LABLE.addr, 40, value);
        }
        #endregion
 




        private void button_loadBootCfg_Click(object sender, EventArgs e)
        {

            pc.status_top = Constants.LOAD_BOOTCFG_TOP_STATUS;
            pc.status_mid = 0;// Constants.EQU_LABLE_STATUS;
            pc.status_low = -1;
            pc.bootcfg_line_num = 0;
            status_handler(pc.status_top, pc.status_mid, pc.status_low);
            button3.Enabled = true;

        }

        private void button_burn_fac_app_Click(object sender, EventArgs e)
        {
            pc.status_top = Constants.BURN_FAC_APP_TOP_STATUS;
            pc.status_mid = 0;// Constants.EQU_LABLE_STATUS;
            pc.status_low = 0;// Constants.BURN_FAC_APP_TOP_STATUS;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;
            status_handler(pc.status_top, pc.status_mid, pc.status_low);

        }

        private void button_update_fac_load_Click(object sender, EventArgs e)
        {
            pc.status_top = Constants.UPDATE_FAC_TOP_STATUS;
            pc.status_mid = 0;// Constants.EQU_LABLE_STATUS;
            pc.status_low = -1;
            pc.write_total_len_in_byte = 0;
            pc.write_finish = 0;
            status_handler(pc.status_top, pc.status_mid, pc.status_low);

        }


        private void button_update_app1_load_Click(object sender, EventArgs e)
        {
            pc.status_top = Constants.UPDATE_APP1_TOP_STATUS;
            pc.status_mid = 0;// Constants.EQU_LABLE_STATUS;
            pc.status_low = -1;
            pc.write_total_len_in_byte = 0;
            pc.write_finish = 0;
            status_handler(pc.status_top, pc.status_mid, pc.status_low);

        }

        private void button_update_app2_load_Click(object sender, EventArgs e)
        {
            pc.status_top = Constants.UPDATE_APP2_TOP_STATUS;
            pc.status_mid = 0;// Constants.EQU_LABLE_STATUS;
            pc.status_low = -1;
            pc.write_total_len_in_byte = 0;
            pc.write_finish = 0;
            status_handler(pc.status_top, pc.status_mid, pc.status_low);

        }

        private void button_burn_boot_fac_app_Click(object sender, EventArgs e)
        {
            pc.status_top = Constants.BURN_BOOT_FAC_APP_TOP_STATUS;
            pc.status_mid = 0;// Constants.EQU_LABLE_STATUS;
            pc.status_low = 0;// Constants.BURN_FAC_APP_TOP_STATUS;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;
            status_handler(pc.status_top, pc.status_mid, pc.status_low);
        }



        private void button_save_image2Disk_Click(object sender, EventArgs e)
        {
            pc.status_top = Constants.SAVE_IMAGE2DISK_TOP_STATUS;
            pc.status_mid = 0;// Constants.EQU_LABLE_STATUS;
            pc.status_low = -1;// Constants.BURN_FAC_APP_TOP_STATUS;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;
            status_handler(pc.status_top, pc.status_mid, pc.status_low);

        }

        private void button_load_image2Flash_Click(object sender, EventArgs e)
        {
            //
            pc.status_top = Constants.LOAD_IMAGE2FLASH_TOP_STATUS;
            pc.status_mid = 0;// Constants.EQU_LABLE_STATUS;
            pc.status_low = -1;// Constants.BURN_FAC_APP_TOP_STATUS;
            pc.write_finish = 0;
            pc.write_total_len_in_byte = 0;
            status_handler(pc.status_top, pc.status_mid, pc.status_low);

        }


        public byte[] string_to_byte(string str, UInt16 length_in_bytes)
        {
            string sub_string1 = str.Trim();
            string[] sub_string2 = sub_string1.Split(' ');
            byte[] ret_arr = new byte[length_in_bytes];
            for (int ii = 0; ii < length_in_bytes; ii++)
            {
                ret_arr[ii] = System.Convert.ToByte(sub_string2[ii], 16);

            }
            return ret_arr;
        }

        public UInt16[] string_to_UInt16(string str, UInt16 length_in_UInt16)
        {
            string sub_string1 = str.Trim();
            string[] sub_string2 = sub_string1.Split(' ');
            UInt16[] ret_arr = new UInt16[length_in_UInt16];
            for (int ii = 0; ii < length_in_UInt16; ii++)
            {
                ret_arr[ii] = System.Convert.ToUInt16(sub_string2[ii], 16);

            }
            return ret_arr;
        }

        public UInt32[] string_to_UInt32(string str, UInt16 length_in_bytes)
        {
           
            string sub_string1 = str.Trim();
            string[] sub_string2 = sub_string1.Split(' ');
            UInt32[] ret_arr = new UInt32[length_in_bytes];
            ret_arr[0] = System.Convert.ToUInt32(sub_string2[0], 16);

            return ret_arr;
        }
        
        public UInt32[] bytestring_to_UInt32(string str, UInt16 length_in_bytes)
        {
            int ii;
            string sub_string1 = str.Trim();
            string[] sub_string2 = sub_string1.Split(' ');
            UInt32[] ret_arr = new UInt32[(length_in_bytes + 3) / 4];
            byte[] tmp = new byte[4] { 0, 0, 0, 0 };
            if (length_in_bytes % 4 == 0)
            {
                for (ii = 0; ii < length_in_bytes; ii += 4)
                {
                    tmp[0] = System.Convert.ToByte(sub_string2[ii], 16);
                    tmp[1] = System.Convert.ToByte(sub_string2[ii + 1], 16);
                    tmp[2] = System.Convert.ToByte(sub_string2[ii + 2], 16);
                    tmp[3] = System.Convert.ToByte(sub_string2[ii + 3], 16);
                    ret_arr[(ii + 0) / 4] = (UInt32)(tmp[0] + (tmp[1] << 8) + (tmp[2] << 16) + (tmp[3] << 24));
                }
            }
            else if (length_in_bytes % 4 == 1)
            {
                for (ii = 0; ii < length_in_bytes; ii += 4)
                {
                    tmp[0] = System.Convert.ToByte(sub_string2[ii], 16);
                    if (ii + 1 < length_in_bytes)
                    {
                        tmp[1] = System.Convert.ToByte(sub_string2[ii + 1], 16);
                        tmp[2] = System.Convert.ToByte(sub_string2[ii + 2], 16);
                        tmp[3] = System.Convert.ToByte(sub_string2[ii + 3], 16);
                    }
                    ret_arr[(ii + 3) / 4] = (UInt32)(tmp[0] + (tmp[1] << 8) + (tmp[2] << 16) + (tmp[3] << 24));
                }
            }
            else if (length_in_bytes % 4 == 2)
            {
                for (ii = 0; ii < length_in_bytes; ii += 4)
                {
                    tmp[0] = System.Convert.ToByte(sub_string2[ii], 16);
                    tmp[1] = System.Convert.ToByte(sub_string2[ii + 1], 16);
                    if (ii + 2 < length_in_bytes)
                    {
                        tmp[2] = System.Convert.ToByte(sub_string2[ii + 2], 16);
                        tmp[3] = System.Convert.ToByte(sub_string2[ii + 3], 16);
                    }
                    ret_arr[(ii + 2) / 4] = (UInt32)(tmp[0] + (tmp[1] << 8) + (tmp[2] << 16) + (tmp[3] << 24));
                }
            }
            else// if (length_in_bytes % 4 == 3)
            {
                for (ii = 0; ii < length_in_bytes; ii += 4)
                {
                    tmp[0] = System.Convert.ToByte(sub_string2[ii], 16);
                    tmp[1] = System.Convert.ToByte(sub_string2[ii + 1], 16);
                    tmp[2] = System.Convert.ToByte(sub_string2[ii + 2], 16);
                    if (ii + 3 < length_in_bytes)
                    {
                        tmp[3] = System.Convert.ToByte(sub_string2[ii + 3], 16);
                    }
                    ret_arr[(ii + 1) / 4] = (UInt32)(tmp[0] + (tmp[1] << 8) + (tmp[2] << 16) + (tmp[3] << 24));
                }
            }

            return ret_arr;
        }



        private void button_about_Click(object sender, EventArgs e)
        {
            MessageBox.Show("This is the fmpt tools version 1.1", "关于FMPT",
                MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            return;
        }

        private void button_bootload2_swrel_set_Click(object sender, EventArgs e)
        {

        }

        private void button_bootload2_chksum_check_Click(object sender, EventArgs e)
        {

        }
        //LC : use this function to get the debug trace to observe and analyse
        private void button1_Click(object sender, EventArgs e)
        {
            string CopyText = "";
            for (int i = 0; i < listBox_debug.Items.Count; i++)
            {

                CopyText = CopyText + listBox_debug.Items[i].ToString() + "\n";
            }
            Clipboard.SetText(CopyText);

        }
        //LC:this function is used to erase the sector


        private void BootCfg_Enter(object sender, EventArgs e)
        {

        }

        private void label32_Click(object sender, EventArgs e)
        {

        }

        private void textBox_equaLable_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox_hwType_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox_hwPemId_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox_swRelId_TextChanged(object sender, EventArgs e)
        {

        }

       
        private void textBox_swUpgradeFlag_TextChanged(object sender, EventArgs e)
        {

        }
        //LC:this function is used to create file 
        private void button4_Click(object sender, EventArgs e)
        {
            {

                // FileStream fs = new FileStream("D:\\bootcfg.txt", FileMode.Open);

                //byte[] data = System.Text.Encoding.Default.GetBytes("Hello World!");
                //fs.Write(data, 0, data.Length);

                string path = "C:\\bootcfg.txt";//file path
                FileStream fs = new FileStream(path, FileMode.Create);
                StreamWriter sw = new StreamWriter(fs);
                sw.WriteLine("equaLable=" + textBox_equaLable.Text);
                sw.WriteLine("hwType=" + textBox_hwType.Text);
                sw.WriteLine("hwPemId=" + textBox_hwPemId.Text);
                sw.WriteLine("swRelId=" + textBox_swRelId.Text);
                sw.WriteLine("swVerId=" + textBox_swVerId.Text);
                sw.WriteLine("swUpgradeFlag=" + textBox_swUpgradeFlag.Text);
                sw.WriteLine("swUpgPollId=" + textBox_swUpgPollId.Text);
                sw.WriteLine("bootIndex=" + textBox_bootIndex.Text);
                sw.WriteLine("bootAreaMax=" + textBox_bootAreaMax.Text);
                sw.WriteLine("cipherKey=" + textBox_cipherKey.Text);
                sw.Close();
                fs.Close();



                //string strs = File.ReadAllText(@"D:\\bootcfg.txt");
                //listBox_debug.Items.Add("" + strs);

                /*  StreamReader reader = new StreamReader("D:\\bootcfg.txt");
                  string line = reader.ReadLine();//从txt文件中读取一行
                  string all = reader.ReadToEnd();//从txt文件中读取全部内容
                  listBox_debug.Items.Add("" + all);
                  listBox_debug.Items.Add("thecontroltable=" + thecontroltable);
                  reader.Close();//关闭文件
                 /* StreamWriter writer = new StreamWriter("D:\\bootcfg.txt");
                  writer.WriteLine(line);//向txt文件中写入一行
                  writer.Write(all);//向txt文件中写入多行
                  writer.Close();//关闭文件*/


            }

        }




        private void Form1_Load(object sender, EventArgs e)
        {

        }
        //LC:add exit function
        private void button5_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void textBox11_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        //LC:the copy button used to copy read value to write value
        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox_equaLable.Text;
            textBox2.Text = textBox_hwType.Text;
            textBox3.Text = textBox_hwPemId.Text;
            textBox4.Text = textBox_swRelId.Text;
            textBox5.Text = textBox_swVerId.Text;
            textBox6.Text = textBox_swUpgradeFlag.Text;
            textBox7.Text = textBox_swUpgPollId.Text;
            textBox8.Text = textBox_bootIndex.Text;
            textBox9.Text = textBox_bootAreaMax.Text;
            textBox10.Text = textBox_cipherKey.Text;
            button_update_bootcfg.Enabled = true;

        }

        private void label20_Click(object sender, EventArgs e)
        {

        }

      
    }

    static class Constants
    {
        public const byte IHU_L2PACKET_START_CHAR = 0xFE;
        public const UInt32 IHU_L2PACKET_RX_STATE_START = 0;
        public const UInt32 IHU_L2PACKET_RX_STATE_HEADER = 1;
        public const UInt32 IHU_L2PACKET_RX_STATE_BODY = 2;
        public const UInt16 HUITP_MSGID_sui_inventory_report = 0xA090;
        public const UInt16 HUITP_MSGID_sui_inventory_confirm = 0xA010;
        public const UInt16 HUITP_MSGID_sui_sw_package_report = 0xA190;
        public const UInt16 HUITP_MSGID_sui_sw_package_confirm = 0xA110;

        public const UInt16 HUITP_MSGID_sui_flash_raw_cmd_req = 0xA290;
        public const UInt16 HUITP_MSGID_sui_flash_raw_cmd_rsp = 0xA210;


        //public const UInt16 RAW_CMD_ID = 0xAAAA;
        public const UInt16 MAX_LEN_FLASH_RAW_COMMAND_DATA = (256 - 4 - 16);
        public const UInt16 MAX_WMC_CONTROL_MSG_LEN = 256;
        public const UInt32 MAX_FLASH_LEN_IN_BYTES = 1024 * 1024;

        //1. flashRawCommandMode: 
        public const byte IAP_FLASH_RAW_COMMAND_MODE_ACTIVE = 1;
        public const byte IAP_FLASH_RAW_COMMAND_MODE_DEACTIVE = 2;

        //2. flashRawCommand:
        public const byte IAP_FLASH_RAW_COMMAND_SECTOR_ERASE = 1;
        public const byte IAP_FLASH_RAW_COMMAND_FLASH_LOCK = 2;
        public const byte IAP_FLASH_RAW_COMMAND_FLASH_UNLOCK = 3;
        public const byte IAP_FLASH_RAW_COMMAND_WRITE = 4;
        public const byte IAP_FLASH_RAW_COMMAND_READ = 5;

        //3.flashRawCommandResp
        public const byte IAP_FLASH_RAW_COMMAND_RESPONSE_OK = 1;
        public const byte IAP_FLASH_RAW_COMMAND_RESPONSE_NOK = 2;
        public const byte IAP_FLASH_RAW_COMMAND_RESPONSE_INVALID_COMMAND = 3;
        public const byte IAP_FLASH_RAW_COMMAND_RESPONSE_INVALID_STATE = 4;

        //flash addr def
        public const UInt32 FLASH_ADDRESS_BASE = 0x08000000;
        public const UInt32 FLASH_ADDRESS_SW_CONTROL_TABLE = 0x080E0000;
        public const UInt32 FLASH_ADDRESS_IAP_LOAD = 0x08000000;
        public const UInt32 FLASH_ADDRESS_FACTORY_LOAD = 0x08020000;
        public const UInt32 FLASH_ADDRESS_APP1_LOAD = 0x08060000;
        public const UInt32 FLASH_ADDRESS_APP2_LOAD = 0x080A0000;

        //flash sec size
        public const UInt32 FLASH_SEC_SW_CONTROL_TABLE_SIZE_IN_BYTES = 128 * 1024;
        public const UInt32 FLASH_SEC_IAP_SIZE_IN_BYTES = 128 * 1024;
        public const UInt32 FLASH_SEC_FAC_SIZE_IN_BYTES = 256 * 1024;
        public const UInt32 FLASH_SEC_APP1_SIZE_IN_BYTES = 256 * 1024;
        public const UInt32 FLASH_SEC_APP2_SIZE_IN_BYTES = 256 * 1024;

        //flash sec def
        public const UInt32 FLASH_START_ADDRESS_SEC0 = 0x08000000;
        public const UInt32 FLASH_START_ADDRESS_SEC1 = 0x08004000;
        public const UInt32 FLASH_START_ADDRESS_SEC2 = 0x08008000;
        public const UInt32 FLASH_START_ADDRESS_SEC3 = 0x0800C000;
        public const UInt32 FLASH_START_ADDRESS_SEC4 = 0x08010000;
        public const UInt32 FLASH_START_ADDRESS_SEC5 = 0x08020000;
        public const UInt32 FLASH_START_ADDRESS_SEC6 = 0x08040000;
        public const UInt32 FLASH_START_ADDRESS_SEC7 = 0x08060000;
        public const UInt32 FLASH_START_ADDRESS_SEC8 = 0x08080000;
        public const UInt32 FLASH_START_ADDRESS_SEC9 = 0x080A0000;
        public const UInt32 FLASH_START_ADDRESS_SEC10 = 0x080C0000;
        public const UInt32 FLASH_START_ADDRESS_SEC11 = 0x080E0000;
        public const UInt32 FLASH_MAX_ADDRESS = 0x080FFFFF;

        public const byte FLASH_SEC0 = 0;
        public const byte FLASH_SEC1 = 1;
        public const byte FLASH_SEC2 = 2;
        public const byte FLASH_SEC3 = 3;
        public const byte FLASH_SEC4 = 4;
        public const byte FLASH_SEC5 = 5;
        public const byte FLASH_SEC6 = 6;
        public const byte FLASH_SEC7 = 7;
        public const byte FLASH_SEC8 = 8;
        public const byte FLASH_SEC9 = 9;
        public const byte FLASH_SEC10 = 10;
        public const byte FLASH_SEC11 = 11;

        //bootcfg bitmap
        public const UInt32 bootcfg_equlabel = 1;
        public const UInt32 bootcfg_hw_type = 2;
        public const UInt32 bootcfg_hw_pem_id = 3;
        public const UInt32 bootcfg_sw_rel_id = 4;
        public const UInt32 bootcfg_sw_ver_id = 5;
        public const UInt32 bootcfg_sw_upgrade_flag = 6;
        public const UInt32 bootcfg_sw_upgrapoll_id = 7;
        public const UInt32 bootcfg_boot_index = 8;
        public const UInt32 bootcfg_boot_area_max = 9;
        public const UInt32 bootcfg_facLoadAddr = 10;
        public const UInt32 bootcfg_facLoadSwRel = 11;
        public const UInt32 bootcfg_facLoadSwVer = 12;
        public const UInt32 bootcfg_facLoadCheckSum = 13;
        public const UInt32 bootcfg_facLoadValid = 14;
        public const UInt32 bootcfg_facLoadLen = 15;
        public const UInt32 bootcfg_bootLoad1Addr = 16;
        public const UInt32 bootcfg_bootLoad1RelId = 17;
        public const UInt32 bootcfg_bootLoad1VerId = 18;
        public const UInt32 bootcfg_bootLoad1CheckSum = 19;
        public const UInt32 bootcfg_bootLoad1Valid = 20;
        public const UInt32 bootcfg_bootLoad1Len = 21;
        public const UInt32 bootcfg_bootLoad2Addr = 22;
        public const UInt32 bootcfg_bootLoad2RelId = 23;
        public const UInt32 bootcfg_bootLoad2VerId = 24;
        public const UInt32 bootcfg_bootLoad2CheckSum = 25;
        public const UInt32 bootcfg_bootLoad2Valid = 26;
        public const UInt32 bootcfg_bootLoad2Len = 27;
        public const UInt32 bootcfg_bootLoad3Addr = 28;
        public const UInt32 bootcfg_bootLoad3RelId = 29;
        public const UInt32 bootcfg_bootLoad3VerId = 30;
        public const UInt32 bootcfg_bootLoad3CheckSum = 31;
        public const UInt32 bootcfg_bootLoad3Valid = 32;
        public const UInt32 bootcfg_bootLoad3Len = 33;

        public const UInt32 bootcfg_cipher_key = 34;
        public const UInt32 bootcfg_rsv = 35;



        //status table
        public const SByte READ_BOOTCFG_STATUS = 0;
        public const SByte ERASE_FAC_STATUS = 10;
        public const SByte WRITE_FAC_STATUS = 11;
        public const SByte ERASE_APP1_STATUS = 12;
        public const SByte WRITE_APP1_STATUS = 13;
        public const SByte ERASE_APP2_STATUS = 14;
        public const SByte WRITE_APP2_STATUS = 15;
        public const SByte UPDATE_FAC_STATUS = 16;
        public const SByte UPDATE_APP1_STATUS = 17;
        public const SByte UPDATE_APP2_STATUS = 18;

        public const SByte ERASE_BOOTCFG_STATUS = 19;
        public const SByte WRITE_BOOTCFG_STATUS = 20;

        public const SByte UPDATE_BOOTCFG_STATUS = 21;

        public const SByte READ_IMAGE2DISK_STATUS = 22;

        public const SByte ERASE_FLASHBOOTCFG_STATUS = 23;
        public const SByte ERASE_FLASHFAC_STATUS = 24;
        public const SByte ERASE_FLASHAPP1_STATUS = 25;
        public const SByte ERASE_FLASHAPP2_STATUS = 26;

        public const SByte WRITE_FLASHBOOTCFG_STATUS = 27;
        public const SByte WRITE_FLASHFAC_STATUS = 28;
        public const SByte WRITE_FLASHAPP1_STATUS = 29;
        public const SByte WRITE_FLASHAPP2_STATUS = 30;

        public const SByte READ_BOOTCFG_ALL_FIELDS_STATUS = 31;
        public const SByte WRITE_BOOTCFG_SINGLE_FIELD_STATUS = 32;

        public const SByte LOAD_BOOTCFG_TOP_STATUS = 0;
        public const SByte UPDATE_BOOTCFG_TOP_STATUS = 1;
        public const SByte UPDATE_FAC_TOP_STATUS = 2;
        public const SByte UPDATE_APP1_TOP_STATUS = 3;
        public const SByte UPDATE_APP2_TOP_STATUS = 4;

        public const SByte BURN_FAC_APP_TOP_STATUS = 5;
        public const SByte BURN_BOOT_FAC_APP_TOP_STATUS = 6;

        public const SByte SAVE_IMAGE2DISK_TOP_STATUS = 7;
        public const SByte LOAD_IMAGE2FLASH_TOP_STATUS = 8;

        public const SByte UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS = 9;

        public const SByte MAX_COL_STATUS = 10;
        public const SByte MAX_ROW_STATUS = 10;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    unsafe public struct msg_struct_l3iap_flash_raw_command_req
    {
        public UInt16 msgid;
        public UInt16 length;
        public byte flashRawCommandMode;
        public byte flashRawCommand;
        public byte flashSectorIdToErase;
        public byte flashSectorNumberToErase;
        public UInt32 flashAddressToAccess;
        public UInt32 flashValidLengthToAccess;
        public fixed byte data[Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA];
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    unsafe public struct msg_struct_l3iap_flash_raw_command_resp
    {
        public UInt16 msgid;
        public UInt16 length;
        public byte flashRawCommandModeResp;
        public byte flashRawCommandResp;
        public byte flashSectorIdToErase;
        public byte flashSectorNumberToErase;
        public UInt32 flashAddressToAccess;
        public UInt32 flashValidLengthToAccess;
        public fixed byte data[Constants.MAX_LEN_FLASH_RAW_COMMAND_DATA];
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct field_def
    {
        public UInt32 addr;
        public UInt32 len;
        //public TextBox dest;
        public SByte valid;
        public field_def(UInt32 a, UInt32 b, SByte d)
        {
            addr = a;
            len = b;
            // dest = c;
            valid = d;
        }
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct process_control
    {
        public SByte status_top;
        public SByte status_mid;
        public SByte status_low;
        //1.for update bootcfg
        public SByte bootcfg_line_num;

        //2.for update fac load
        //public UInt32 fac_load_write_addr;
        //public UInt32 fac_load_write_len;
        public UInt32 write_total_len_in_byte;
        public UInt32 write_finish;

        public process_control(SByte a, SByte b, SByte c, SByte d, UInt32 e, UInt32 f)
        {
            status_top = a;
            status_mid = b;
            status_low = c;
            bootcfg_line_num = d;
            // fac_load_write_addr = e;
            // fac_load_write_len = f;
            write_total_len_in_byte = e;
            write_finish = f;

        }
    }
}


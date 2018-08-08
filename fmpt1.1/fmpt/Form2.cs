using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

//5.瀹氫箟鍒濆鍖朇AN鐨勬暟鎹被鍨?
public struct VCI_INIT_CONFIG
{
    public UInt32 AccCode;
    public UInt32 AccMask;
    public UInt32 Reserved;
    public byte Filter;   //1鎺ユ敹鎵€鏈夊抚銆?鏍囧噯甯ф护娉紝3鏄墿灞曞抚婊ゆ尝銆?
    public byte Timing0;
    public byte Timing1;
    public byte Mode;     //妯″紡锛?琛ㄧず姝ｅ父妯″紡锛?琛ㄧず鍙惉妯″紡,2鑷祴妯″紡
}



namespace fmpt
{
    public partial class Form2 : Form
    {
        public UInt32 m_devtype = 4;//USBCAN2
        public static UInt32 m_bOpen = 0;
        public UInt32 m_devind = 0;
        public UInt32 m_canind = 0;
        const int DEV_USBCAN = 3;//3;
        const int DEV_USBCAN2 = 2;//4;
        UInt32[] m_arrdevtype = new UInt32[20];
        /*------------鍏煎ZLG鐨勫嚱鏁版弿杩?--------------------------------*/
        [DllImport("controlcan.dll")]
        static extern UInt32 VCI_OpenDevice(UInt32 DeviceType, UInt32 DeviceInd, UInt32 Reserved);
        [DllImport("controlcan.dll")]
        static extern UInt32 VCI_CloseDevice(UInt32 DeviceType, UInt32 DeviceInd);
        [DllImport("controlcan.dll")]
        static extern UInt32 VCI_InitCAN(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd, ref VCI_INIT_CONFIG pInitConfig);
        [DllImport("controlcan.dll")]
        static extern UInt32 VCI_StartCAN(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd);
        [DllImport("controlcan.dll")]
        static extern UInt32 VCI_ResetCAN(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd);

        public Form2()
        {
            InitializeComponent();
        }
        private void Form2_Load(object sender, EventArgs e)
        {
        
            
            Form1 main = (Form1)this.Owner;
            comboBox_DevIndex.SelectedIndex = 0;
            comboBox_CANIndex.SelectedIndex = 0;
            textBox_AccCode.Text = "80000000";
            textBox_AccMask.Text = "FFFFFFFF";
            textBox_Time0.Text = "00";
            textBox_Time1.Text = "1C";
            comboBox_Filter.SelectedIndex = 0;              //鎺ユ敹鎵€鏈夌被鍨?
            comboBox_Mode.SelectedIndex = 0;                //0:姝ｅ父锛?:杩樺洖娴嬭瘯妯″紡
            comboBox_FrameFormat.SelectedIndex = 0;
            comboBox_FrameType.SelectedIndex = 1;
            textBox_ID.Text = "00100001";//"00000602";

            buttonConnect.Text = main.bopen == 1 ? "断开" : "连接";
            m_bOpen = main.bopen;
            //
            Int32 curindex = 0;
            comboBox_devtype.Items.Clear();

            curindex = comboBox_devtype.Items.Add("DEV_USBCAN");
            m_arrdevtype[curindex] = DEV_USBCAN;
            //comboBox_devtype.Items[2] = "VCI_USBCAN1";
            //m_arrdevtype[2]=  VCI_USBCAN1 ;

            curindex = comboBox_devtype.Items.Add("DEV_USBCAN2");
            m_arrdevtype[curindex] = DEV_USBCAN2;
            //comboBox_devtype.Items[3] = "VCI_USBCAN2";
            //m_arrdevtype[3]=  VCI_USBCAN2 ;

            comboBox_devtype.SelectedIndex = 0;
            comboBox_devtype.MaxDropDownItems = comboBox_devtype.Items.Count;

        }

        private void Form2_FormClosed(object sender, FormClosedEventArgs e)
        {
            /*if (m_bOpen == 1)
            {
                VCI_CloseDevice(m_devtype, m_devind);
            }*/
        }
       
        unsafe private void buttonConnect_Click(object sender, EventArgs e)
        {

        	Form1 main = (Form1)this.Owner;
            if (m_bOpen == 1)
            {
                VCI_CloseDevice(m_devtype, m_devind);
                m_bOpen = 0;
            }
            else
            {
                m_devtype = m_arrdevtype[comboBox_devtype.SelectedIndex];

                m_devind = (UInt32)comboBox_DevIndex.SelectedIndex;
                m_canind = (UInt32)comboBox_CANIndex.SelectedIndex;//(UInt32)0x00200001U;//= 
                if (VCI_OpenDevice(m_devtype, m_devind, 0) == 0)
                {
                    MessageBox.Show("打开设备失败,请检查设备类型和设备索引号是否正确", "错误",
                            MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                    return;
                }
                main.button_loadBootCfg.Enabled = true;    //LC:bug fixed
                m_bOpen = 1;
                VCI_INIT_CONFIG config = new VCI_INIT_CONFIG();
                config.AccCode = System.Convert.ToUInt32("0x" + textBox_AccCode.Text, 16);
                config.AccMask = System.Convert.ToUInt32("0x" + textBox_AccMask.Text, 16);
                config.Timing0 = System.Convert.ToByte("0x" + textBox_Time0.Text, 16);
                config.Timing1 = System.Convert.ToByte("0x" + textBox_Time1.Text, 16);
                config.Filter = (Byte)(comboBox_Filter.SelectedIndex + 1);
                config.Mode = (Byte)comboBox_Mode.SelectedIndex;
				main.frame_desc.RxState = 0;
           /* fixed (byte* rxBuf = &main.g_can_rx_buffer[0])
            {
                main.frame_desc.pRxBuffPtr = rxBuf;
            }*/
            
            main.frame_desc.RxBuffSize = 256;
            main.frame_desc.RxXferCount = 0;
                VCI_InitCAN(m_devtype, m_devind, m_canind, ref config);
				VCI_StartCAN(m_devtype, m_devind, m_canind);
            }
            buttonConnect.Text = m_bOpen == 1 ? "断开" : "连接";

            main.remoteflag = comboBox_FrameFormat.SelectedIndex;
            main.extflag = comboBox_FrameType.SelectedIndex;
            main.id = textBox_ID.Text;
            main.devtype = m_devtype;
            main.devind = m_devind;
            main.canind = m_canind;
            main.bopen = m_bOpen;
            main.timer_rec.Enabled = (m_bOpen == 1) ? true : false;
            main.listBox_debug.Items.Clear();
			
			main.listBox_debug.Items.Add("setup transport, open=" + System.Convert.ToString(m_bOpen, 16));
			main.listBox_debug.SelectedIndex = main.listBox_debug.Items.Count - 1;

        }

        private void textBox_ID_TextChanged(object sender, EventArgs e)
        {

        }
    }
}

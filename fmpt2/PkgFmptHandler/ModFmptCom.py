'''
Created on 2018/2/25

#
MODDULE: FMPT2 COMMON MODULES

@author: hitpony
'''

#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

import random
import sys
import time
import json
import os
import re
import urllib
import http
import socket


#Boot cfg engineering data
zStrBootCfgEng = {\
    "equLable": "IHU_G5104GTJY_SH001",\
    "hwType": 0,\
    "hwPemId": 0,\
    "swRelId": 0,\
    "swVerId": 0,\
    "swUpgradeFlag": 0,\
    "swUpgPollId": 0,\
    "bootIndex": 0,\
    "bootAreaMax": 0,\
    "facLoadAddr": 0,\
    "facLoadSwRel": 0,\
    "facLoadSwVer": 0,\
    "facLoadCheckSum": 0,\
    "facLoadValid": 0,\
    "facLoadLen": 0,\
    "bootLoad1Addr": 0,\
    "bootLoad1RelId": 0,\
    "bootLoad1VerId": 0,\
    "bootLoad1CheckSum": 0,\
    "bootLoad1Valid": 0,\
    "bootLoad1Len": 0,\
    "bootLoad2Addr": 0,\
    "bootLoad2RelId": 0,\
    "bootLoad2VerId": 0,\
    "bootLoad2CheckSum": 0,\
    "bootLoad2Valid": 0,\
    "bootLoad2Len": 0,\
    "bootLoad3Addr": 0,\
    "bootLoad3RelId": 0,\
    "bootLoad3VerId": 0,\
    "bootLoad3CheckSum": 0,\
    "bootLoad3Valid": 0,\
    "bootLoad3Len": 0,\
    "cipherKey": [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F],\
    "rsv": [0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F]
    }

GL_FMPT_BOOT_CFG_LOCAL_FILE_NAME       = 'd:/bootcfg.txt';
GL_FMPT_BOOT_CFG_LOCAL_FILE_TYPE       = '.txt';

#Init address and configuration
GL_FMPT_BOOT_CFG_ENG_ADDR = {\
    "equLable": (0x080E0000, 20 , 1),\
    "hwType": (0x080E0014, 2,  1),\
    "hwPemId": (0x080E0016, 2,  1),\
    "swRelId": (0x080E0018, 2,  1),\
    "swVerId": (0x080E001A, 2,  1),\
    "swUpgradeFlag": (0x080E001C, 1,  1),\
    "swUpgPollId": (0x080E001D, 1,  1),\
    "bootIndex": (0x080E001E, 1,  1),\
    "bootAreaMax": (0x080E001F, 1,  1),\
    "facLoadAddr": (0x080E0020, 4,  1),\
    "facLoadSwRel": (0x080E0024, 2,  1),\
    "facLoadSwVer": (0x080E0026, 2,  1),\
    "facLoadCheckSum": (0x080E0028, 2,  1),\
    "facLoadValid": (0x080E002A, 2,  1),\
    "facLoadLen": (0x080E002C, 4,  1),\
    "bootLoad1Addr": (0x080E0030, 4,  1),\
    "bootLoad1RelId": (0x080E0034, 2,  1),\
    "bootLoad1VerId": (0x080E0036, 2,  1),\
    "bootLoad1CheckSum": (0x080E0038, 2,  1),\
    "bootLoad1Valid": (0x080E003A, 2,  1),\
    "bootLoad1Len": (0x080E003C, 4,  1),\
    "bootLoad2Addr": (0x080E0040, 4,  1),\
    "bootLoad2RelId": (0x080E0044, 2,  1),\
    "bootLoad2VerId": (0x080E0046, 2,  1),\
    "bootLoad2CheckSum": (0x080E0048, 2,  1),\
    "bootLoad2Valid": (0x080E004A, 2,  1),\
    "bootLoad2Len": (0x080E004C, 4,  1),\
    "bootLoad3Addr": (0x080E0050, 4,  0),\
    "bootLoad3RelId": (0x080E0054, 2,  0),\
    "bootLoad3VerId": (0x080E0056, 2,  0),\
    "bootLoad3CheckSum": (0x080E0058, 2,  0),\
    "bootLoad3Valid": (0x080E005A, 2,  0),\
    "bootLoad3Len": (0x080E005C, 4,  0),\
    "cipherKey": (0x080E0060, 16,  1),\
    "rsv": (0x080E0070, 16,  0)\
    }

GL_FMPT_BOOT_CFG_ENG_TOTAL_LEN = 128;

#Global const setting
GL_FMPT_IHU_L2PACKET_START_CHAR = 0xFE;
# GL_FMPT_IHU_L2PACKET_RX_STATE_START = 0;
# GL_FMPT_IHU_L2PACKET_RX_STATE_HEADER = 1;
# GL_FMPT_IHU_L2PACKET_RX_STATE_BODY = 2;
GL_FMPT_HUITP_MSGID_sui_inventory_report = 0xA090;
GL_FMPT_HUITP_MSGID_sui_inventory_confirm = 0xA010;
GL_FMPT_HUITP_MSGID_sui_sw_package_report = 0xA190;
GL_FMPT_HUITP_MSGID_sui_sw_package_confirm = 0xA110;
GL_FMPT_HUITP_MSGID_sui_flash_raw_cmd_req = 0xA290;
GL_FMPT_HUITP_MSGID_sui_flash_raw_cmd_rsp = 0xA210;

#public const UInt16 RAW_CMD_ID = 0xAAAA;
GL_FMPT_MAX_GEN_CONTROL_MSG_LEN = 256;
GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA = (GL_FMPT_MAX_GEN_CONTROL_MSG_LEN-4-16);
GL_FMPT_MAX_FLASH_LEN_IN_BYTES = 1024 * 1024;

#1. flashRawCommandMode: 
GL_FMPT_IAP_FLASH_RAW_COMMAND_MODE_ACTIVE = 1;
GL_FMPT_IAP_FLASH_RAW_COMMAND_MODE_DEACTIVE = 2;

#2. flashRawCommand:
GL_FMPT_IAP_FLASH_RAW_COMMAND_SECTOR_ERASE = 1;
GL_FMPT_IAP_FLASH_RAW_COMMAND_FLASH_LOCK = 2;
GL_FMPT_IAP_FLASH_RAW_COMMAND_FLASH_UNLOCK = 3;
GL_FMPT_IAP_FLASH_RAW_COMMAND_WRITE = 4;
GL_FMPT_IAP_FLASH_RAW_COMMAND_READ = 5;

#3.flashRawCommandResp
GL_FMPT_IAP_FLASH_RAW_COMMAND_RESPONSE_OK = 1;
GL_FMPT_IAP_FLASH_RAW_COMMAND_RESPONSE_NOK = 2;
GL_FMPT_IAP_FLASH_RAW_COMMAND_RESPONSE_INVALID_COMMAND = 3;
GL_FMPT_IAP_FLASH_RAW_COMMAND_RESPONSE_INVALID_STATE = 4;

#flash addr def
GL_FMPT_FLASH_ADDRESS_BASE = 0x08000000;
GL_FMPT_FLASH_ADDRESS_SW_CONTROL_TABLE = 0x080E0000;
GL_FMPT_FLASH_ADDRESS_IAP_LOAD = 0x08000000;
GL_FMPT_FLASH_ADDRESS_FACTORY_LOAD = 0x08020000;
GL_FMPT_FLASH_ADDRESS_APP1_LOAD = 0x08060000;
GL_FMPT_FLASH_ADDRESS_APP2_LOAD = 0x080A0000;

#flash sec size
GL_FMPT_FLASH_SEC_SW_CONTROL_TABLE_SIZE_IN_BYTES = 128 * 1024;
GL_FMPT_FLASH_SEC_IAP_SIZE_IN_BYTES = 128 * 1024;
GL_FMPT_FLASH_SEC_FAC_SIZE_IN_BYTES = 256 * 1024;
GL_FMPT_FLASH_SEC_APP1_SIZE_IN_BYTES = 256 * 1024;
GL_FMPT_FLASH_SEC_APP2_SIZE_IN_BYTES = 256 * 1024;

#flash sec def
GL_FMPT_FLASH_START_ADDRESS_SEC0 = 0x08000000;
GL_FMPT_FLASH_START_ADDRESS_SEC1 = 0x08004000;
GL_FMPT_FLASH_START_ADDRESS_SEC2 = 0x08008000;
GL_FMPT_FLASH_START_ADDRESS_SEC3 = 0x0800C000;
GL_FMPT_FLASH_START_ADDRESS_SEC4 = 0x08010000;
GL_FMPT_FLASH_START_ADDRESS_SEC5 = 0x08020000;
GL_FMPT_FLASH_START_ADDRESS_SEC6 = 0x08040000;
GL_FMPT_FLASH_START_ADDRESS_SEC7 = 0x08060000;
GL_FMPT_FLASH_START_ADDRESS_SEC8 = 0x08080000;
GL_FMPT_FLASH_START_ADDRESS_SEC9 = 0x080A0000;
GL_FMPT_FLASH_START_ADDRESS_SEC10 = 0x080C0000;
GL_FMPT_FLASH_START_ADDRESS_SEC11 = 0x080E0000;
GL_FMPT_FLASH_MAX_ADDRESS = 0x080FFFFF;

GL_FMPT_FLASH_SEC0 = 0;
GL_FMPT_FLASH_SEC1 = 1;
GL_FMPT_FLASH_SEC2 = 2;
GL_FMPT_FLASH_SEC3 = 3;
GL_FMPT_FLASH_SEC4 = 4;
GL_FMPT_FLASH_SEC5 = 5;
GL_FMPT_FLASH_SEC6 = 6;
GL_FMPT_FLASH_SEC7 = 7;
GL_FMPT_FLASH_SEC8 = 8;
GL_FMPT_FLASH_SEC9 = 9;
GL_FMPT_FLASH_SEC10 = 10;
GL_FMPT_FLASH_SEC11 = 11;

#bootcfg bitmap
GL_FMPT_bootcfg_equlabel = 1;
GL_FMPT_bootcfg_hw_type = 2;
GL_FMPT_bootcfg_hw_pem_id = 3;
GL_FMPT_bootcfg_sw_rel_id = 4;
GL_FMPT_bootcfg_sw_ver_id = 5;
GL_FMPT_bootcfg_sw_upgrade_flag = 6;
GL_FMPT_bootcfg_sw_upgrapoll_id = 7;
GL_FMPT_bootcfg_boot_index = 8;
GL_FMPT_bootcfg_boot_area_max = 9;
GL_FMPT_bootcfg_facLoadAddr = 10;
GL_FMPT_bootcfg_facLoadSwRel = 11;
GL_FMPT_bootcfg_facLoadSwVer = 12;
GL_FMPT_bootcfg_facLoadCheckSum = 13;
GL_FMPT_bootcfg_facLoadValid = 14;
GL_FMPT_bootcfg_facLoadLen = 15;
GL_FMPT_bootcfg_bootLoad1Addr = 16;
GL_FMPT_bootcfg_bootLoad1RelId = 17;
GL_FMPT_bootcfg_bootLoad1VerId = 18;
GL_FMPT_bootcfg_bootLoad1CheckSum = 19;
GL_FMPT_bootcfg_bootLoad1Valid = 20;
GL_FMPT_bootcfg_bootLoad1Len = 21;
GL_FMPT_bootcfg_bootLoad2Addr = 22;
GL_FMPT_bootcfg_bootLoad2RelId = 23;
GL_FMPT_bootcfg_bootLoad2VerId = 24;
GL_FMPT_bootcfg_bootLoad2CheckSum = 25;
GL_FMPT_bootcfg_bootLoad2Valid = 26;
GL_FMPT_bootcfg_bootLoad2Len = 27;
GL_FMPT_bootcfg_bootLoad3Addr = 28;
GL_FMPT_bootcfg_bootLoad3RelId = 29;
GL_FMPT_bootcfg_bootLoad3VerId = 30;
GL_FMPT_bootcfg_bootLoad3CheckSum = 31;
GL_FMPT_bootcfg_bootLoad3Valid = 32;
GL_FMPT_bootcfg_bootLoad3Len = 33;
GL_FMPT_bootcfg_cipher_key = 34;
GL_FMPT_bootcfg_rsv = 35;
GL_FMPT_bootcfg_all = 36;
GL_FMPT_bootcfg_byte_opr = 37;
GL_FMPT_bootcfg_appImage = 38;

#status table
# GL_FMPT_READ_BOOTCFG_STATUS = 0;
# GL_FMPT_ERASE_FAC_STATUS = 10;
# GL_FMPT_WRITE_FAC_STATUS = 11;
# GL_FMPT_ERASE_APP1_STATUS = 12;
# GL_FMPT_WRITE_APP1_STATUS = 13;
# GL_FMPT_ERASE_APP2_STATUS = 14;
# GL_FMPT_WRITE_APP2_STATUS = 15;
# GL_FMPT_UPDATE_FAC_STATUS = 16;
# GL_FMPT_UPDATE_APP1_STATUS = 17;
# GL_FMPT_UPDATE_APP2_STATUS = 18;
# GL_FMPT_ERASE_BOOTCFG_STATUS = 19;
# GL_FMPT_WRITE_BOOTCFG_STATUS = 20;
# GL_FMPT_UPDATE_BOOTCFG_STATUS = 21;
# GL_FMPT_READ_IMAGE2DISK_STATUS = 22;
# GL_FMPT_ERASE_FLASHBOOTCFG_STATUS = 23;
# GL_FMPT_ERASE_FLASHFAC_STATUS = 24;
# GL_FMPT_ERASE_FLASHAPP1_STATUS = 25;
# GL_FMPT_ERASE_FLASHAPP2_STATUS = 26;
# GL_FMPT_WRITE_FLASHBOOTCFG_STATUS = 27;
# GL_FMPT_WRITE_FLASHFAC_STATUS = 28;
# GL_FMPT_WRITE_FLASHAPP1_STATUS = 29;
# GL_FMPT_WRITE_FLASHAPP2_STATUS = 30;
# GL_FMPT_READ_BOOTCFG_ALL_FIELDS_STATUS = 31;
# GL_FMPT_WRITE_BOOTCFG_SINGLE_FIELD_STATUS = 32;
# GL_FMPT_LOAD_BOOTCFG_TOP_STATUS = 0;
# GL_FMPT_UPDATE_BOOTCFG_TOP_STATUS = 1;
# GL_FMPT_UPDATE_FAC_TOP_STATUS = 2;
# GL_FMPT_UPDATE_APP1_TOP_STATUS = 3;
# GL_FMPT_UPDATE_APP2_TOP_STATUS = 4;
# GL_FMPT_BURN_FAC_APP_TOP_STATUS = 5;
# GL_FMPT_BURN_BOOT_FAC_APP_TOP_STATUS = 6;
# GL_FMPT_SAVE_IMAGE2DISK_TOP_STATUS = 7;
# GL_FMPT_LOAD_IMAGE2FLASH_TOP_STATUS = 8;
# GL_FMPT_UPDATE_BOOTCFG_SINGLE_FIELD_TOP_STATUS = 9;
# GL_FMPT_MAX_COL_STATUS = 10;
# GL_FMPT_MAX_ROW_STATUS = 10;  

#Small and Big Endian defination
GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL = 1;
GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_BIG = 2;
GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET = GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL

#Max time to wait IhuCon feedback in number of 10ms
GL_FMPT_IHUCON_WAIT_FB_MAX_IN_MS = 100;
GL_FMPT_IHUCON_DATA_RCV_MAX_LEN = 1000;
GL_FMPT_IHUCON_FRAME_RCV_MAX_LEN = int(GL_FMPT_IHUCON_DATA_RCV_MAX_LEN/8)+1;

#CLOUD SERVER INFO
GL_FMPT_CLOUDCON_PAR_APPLY_NUMBER_SET_DEFAULT = 1;
GL_FMPT_CLOUDCON_PAR_APPLY_NUMBER_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_APPLY_NUMBER_SET_DEFAULT;
GL_FMPT_CLOUDCON_PAR_IP_ADDR_SET_DEFAULT = "120.55.125.100";
GL_FMPT_CLOUDCON_PAR_IP_ADDR_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_IP_ADDR_SET_DEFAULT;
GL_FMPT_CLOUDCON_PAR_FAC_CODE_SET_DEFAULT = "FAC#123";
GL_FMPT_CLOUDCON_PAR_FAC_CODE_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_FAC_CODE_SET_DEFAULT;
GL_FMPT_CLOUDCON_PAR_PD_CODE_SET_DEFAULT = "G201";
GL_FMPT_CLOUDCON_PAR_PD_CODE_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_PD_CODE_SET_DEFAULT;
GL_FMPT_CLOUDCON_PAR_PJ_CODE_SET_DEFAULT = "GTJY";
GL_FMPT_CLOUDCON_PAR_PJ_CODE_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_PJ_CODE_SET_DEFAULT;
GL_FMPT_HUITP_IEID_UNI_EQULABEL_APPLY_USER_INFO_HCU = 1;
GL_FMPT_HUITP_IEID_UNI_EQULABEL_APPLY_USER_INFO_IHU = 2;
GL_FMPT_CLOUDCON_PAR_PD_TYPE_SET_DEFAULT = GL_FMPT_HUITP_IEID_UNI_EQULABEL_APPLY_USER_INFO_IHU;
GL_FMPT_CLOUDCON_PAR_PD_TYPE_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_PD_TYPE_SET_DEFAULT;
GL_FMPT_CLOUDCON_PAR_USER_CODE_SET_DEFAULT = "SH";
GL_FMPT_CLOUDCON_PAR_USER_CODE_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_USER_CODE_SET_DEFAULT;
GL_FMPT_CLOUDCON_PAR_USER_ACCOUNT_SET_DEFAULT = "user1234";
GL_FMPT_CLOUDCON_PAR_USER_ACCOUNT_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_USER_ACCOUNT_SET_DEFAULT;
GL_FMPT_CLOUDCON_PAR_PASSWD_SET_DEFAULT = "user#1234";
GL_FMPT_CLOUDCON_PAR_PASSWD_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_PASSWD_SET_DEFAULT;
GL_FMPT_CLOUDCON_PAR_FORMAL_FLAG_DEFAULT = "Y";
GL_FMPT_CLOUDCON_PAR_FORMAL_FLAG_SET_BY_USER = GL_FMPT_CLOUDCON_PAR_FORMAL_FLAG_DEFAULT;
GL_FMPT_CLOUDCON_HUITP_LOCAL_DEVID_DEFAULT = "IHU_G5014GTJY_RND01";
GL_FMPT_CLOUDCON_HUITP_SVR_NAME_DEFAULT = "XHZN";
GL_FMPT_CLOUDCON_HUITP_MSG_FORMAT = "huitp-json";
GL_FMPT_CLOUDCON_HUITP_JSON_PORT = '9517';
GL_FMPT_HUITP_IEID_UNI_EQULABLE_INSERVICE_INFO_START = 1;
GL_FMPT_HUITP_IEID_UNI_EQULABLE_INSERVICE_INFO_STOP = 2;
GL_FMPT_HUITP_IEID_UNI_EQULABLE_INSERVICE_INFO_SET = GL_FMPT_HUITP_IEID_UNI_EQULABLE_INSERVICE_INFO_START;
GL_FMPT_HUITP_MSGID_uni_equlabel_apply_req               = 0xA200;
GL_FMPT_HUITP_MSGID_uni_equlabel_apply_resp              = 0xA280;
GL_FMPT_HUITP_MSGID_uni_equlabel_apply_report            = 0xA281;
GL_FMPT_HUITP_MSGID_uni_equlabel_apply_confirm           = 0xA201;
GL_FMPT_HUITP_MSGID_uni_equlabel_inservice_req           = 0xA202;
GL_FMPT_HUITP_MSGID_uni_equlabel_inservice_resp          = 0xA282;
GL_FMPT_HUITP_MSGID_uni_equlabel_inservice_report        = 0xA283;
GL_FMPT_HUITP_MSGID_uni_equlabel_inservice_confirm       = 0xA203;

#FILE IMAGE OPERATION
GL_FMPT_FIO_IMAGE_LOCAL_FILE_NAME       = 'd:/a.img';
GL_FMPT_FIO_IMAGE_LOCAL_FILE_TYPE       = '.img';

#Application Image Management
GL_FMPT_AIM_FAC_IMAGE_LOCAL_FILE_NAME       = 'd:/fac.bin';
GL_FMPT_AIM_FAC_IMAGE_LOCAL_FILE_TYPE       = '.bin';
GL_FMPT_AIM_APP1_IMAGE_LOCAL_FILE_NAME       = 'd:/app1.bin';
GL_FMPT_AIM_APP1_IMAGE_LOCAL_FILE_TYPE       = '.bin';
GL_FMPT_AIM_APP2_IMAGE_LOCAL_FILE_NAME       = 'd:/app2.bin';
GL_FMPT_AIM_APP2_IMAGE_LOCAL_FILE_TYPE       = '.bin';
GL_FMPT_AIM_APP3_IMAGE_LOCAL_FILE_NAME       = 'd:/app3.bin';
GL_FMPT_AIM_APP3_IMAGE_LOCAL_FILE_TYPE       = '.bin';

#IHU DEVICE PARAMETERS
GL_FMPT_DEVDRIVE_CAN_DEVTYPE  = 0;  #Type
GL_FMPT_DEVDRIVE_CAN_DEVIND   = 0;  #Index
GL_FMPT_DEVDRIVE_CAN_CANIND   = 0;  #CanId
GL_FMPT_DEVDRIVE_CAN_RCVCODE   = 0;
GL_FMPT_DEVDRIVE_CAN_MASKCODE   = 0;
GL_FMPT_DEVDRIVE_CAN_TIMER0   = 0;
GL_FMPT_DEVDRIVE_CAN_TIMER1   = 0;
GL_FMPT_DEVDRIVE_CAN_FILTER   = 0;
GL_FMPT_DEVDRIVE_CAN_WORKMODE   = 0;
GL_FMPT_DEVDRIVE_CAN_TIMER0   = 0;
GL_FMPT_DEVDRIVE_CAN_REMOTE_FLAG   = 0; #FrameForamt
GL_FMPT_DEVDRIVE_CAN_EXT_FLAG   = 0;  #FrameType
GL_FMPT_DEVDRIVE_CAN_ID   = 0;


#Common Function
class ClassComProc(object):

    #Init this class
    def __init__(self):
        pass


    def FuncLoadBootCfgFileDataIntoMemory(self, bootCfgInput):
        if ('equLable' in bootCfgInput):
            zStrBootCfgEng['equLable'] = bootCfgInput['equLable'];
        if ('hwType' in bootCfgInput):
            zStrBootCfgEng['hwType'] = bootCfgInput['hwType'];
        if ('hwPemId' in bootCfgInput):
            zStrBootCfgEng['hwPemId'] = bootCfgInput['hwPemId'];
        if ('swRelId' in bootCfgInput):
            zStrBootCfgEng['swRelId'] = bootCfgInput['swRelId'];
        if ('swVerId' in bootCfgInput):
            zStrBootCfgEng['swVerId'] = bootCfgInput['swVerId'];
        if ('swUpgradeFlag' in bootCfgInput):
            zStrBootCfgEng['swUpgradeFlag'] = bootCfgInput['swUpgradeFlag'];
        if ('swUpgPollId' in bootCfgInput):
            zStrBootCfgEng['swUpgPollId'] = bootCfgInput['swUpgPollId'];
        if ('bootIndex' in bootCfgInput):
            zStrBootCfgEng['bootIndex'] = bootCfgInput['bootIndex'];
        if ('bootAreaMax' in bootCfgInput):
            zStrBootCfgEng['bootAreaMax'] = bootCfgInput['bootAreaMax'];
        if ('facLoadAddr' in bootCfgInput):
            zStrBootCfgEng['facLoadAddr'] = bootCfgInput['facLoadAddr'];
        if ('facLoadSwRel' in bootCfgInput):
            zStrBootCfgEng['facLoadSwRel'] = bootCfgInput['facLoadSwRel'];
        if ('facLoadSwVer' in bootCfgInput):
            zStrBootCfgEng['facLoadSwVer'] = bootCfgInput['facLoadSwVer'];
        if ('facLoadCheckSum' in bootCfgInput):
            zStrBootCfgEng['facLoadCheckSum'] = bootCfgInput['facLoadCheckSum'];
        if ('facLoadValid' in bootCfgInput):
            zStrBootCfgEng['facLoadValid'] = bootCfgInput['facLoadValid'];
        if ('facLoadLen' in bootCfgInput):
            zStrBootCfgEng['facLoadLen'] = bootCfgInput['facLoadLen'];
        if ('bootLoad1Addr' in bootCfgInput):
            zStrBootCfgEng['bootLoad1Addr'] = bootCfgInput['bootLoad1Addr'];
        if ('bootLoad1RelId' in bootCfgInput):
            zStrBootCfgEng['bootLoad1RelId'] = bootCfgInput['bootLoad1RelId'];
        if ('bootLoad1VerId' in bootCfgInput):
            zStrBootCfgEng['bootLoad1VerId'] = bootCfgInput['bootLoad1VerId'];
        if ('bootLoad1CheckSum' in bootCfgInput):
            zStrBootCfgEng['bootLoad1CheckSum'] = bootCfgInput['bootLoad1CheckSum'];
        if ('bootLoad1Valid' in bootCfgInput):
            zStrBootCfgEng['bootLoad1Valid'] = bootCfgInput['bootLoad1Valid'];
        if ('bootLoad1Len' in bootCfgInput):
            zStrBootCfgEng['bootLoad1Len'] = bootCfgInput['bootLoad1Len'];
        if ('bootLoad2Addr' in bootCfgInput):
            zStrBootCfgEng['bootLoad2Addr'] = bootCfgInput['bootLoad2Addr'];
        if ('bootLoad2RelId' in bootCfgInput):
            zStrBootCfgEng['bootLoad2RelId'] = bootCfgInput['bootLoad2RelId'];
        if ('bootLoad2VerId' in bootCfgInput):
            zStrBootCfgEng['bootLoad2VerId'] = bootCfgInput['bootLoad2VerId'];
        if ('bootLoad2CheckSum' in bootCfgInput):
            zStrBootCfgEng['bootLoad2CheckSum'] = bootCfgInput['bootLoad2CheckSum'];
        if ('bootLoad2Valid' in bootCfgInput):
            zStrBootCfgEng['bootLoad2Valid'] = bootCfgInput['bootLoad2Valid'];
        if ('bootLoad2Len' in bootCfgInput):
            zStrBootCfgEng['bootLoad2Len'] = bootCfgInput['bootLoad2Len'];
        if ('bootLoad3Addr' in bootCfgInput):
            zStrBootCfgEng['bootLoad3Addr'] = bootCfgInput['bootLoad3Addr'];
        if ('bootLoad3RelId' in bootCfgInput):
            zStrBootCfgEng['bootLoad3RelId'] = bootCfgInput['bootLoad3RelId'];
        if ('bootLoad3VerId' in bootCfgInput):
            zStrBootCfgEng['bootLoad3VerId'] = bootCfgInput['bootLoad3VerId'];
        if ('bootLoad3CheckSum' in bootCfgInput):
            zStrBootCfgEng['bootLoad3CheckSum'] = bootCfgInput['bootLoad3CheckSum'];
        if ('bootLoad3Valid' in bootCfgInput):
            zStrBootCfgEng['bootLoad3Valid'] = bootCfgInput['bootLoad3Valid'];
        if ('bootLoad3Len' in bootCfgInput):
            zStrBootCfgEng['bootLoad3Len'] = bootCfgInput['bootLoad3Len'];
        if ('cipherKey' in bootCfgInput):
            zStrBootCfgEng['cipherKey'] = bootCfgInput['cipherKey'];
        if ('rsv' in bootCfgInput):
            zStrBootCfgEng['rsv'] = bootCfgInput['rsv'];
        return 1;
 





        
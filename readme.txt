====HUICLOUD=====
















//=ZJL, 2019 Jan30, CURRENT_SW_DELIVERY R1.42 =>HST
= 增加DjangDB的设置与配置，方便各种条件下的共融性


//=ZJL, 2019 Jan29, CURRENT_SW_DELIVERY R1.41 =>HST
= 修正主服务中的一个BUG: class ClassHttpRequestGenernalHandler(BaseHTTPRequestHandler)不能有__init__()函数，不然一堆问题
= 先主要采用hst_curlib3_client_connection()来喂UT消息

//=ZJL, 2018 Dec.5, CURRENT_SW_DELIVERY R1.40 =>HST
= 增加MDC模块
= 建立项目与激活模块的关联关系

//=ZJL, 2018 Dec.4, CURRENT_SW_DELIVERY R1.39 =>HST
= 准备完善多分支的合并：后台服务器使用的版本，HCU下的兼容，WINDOWS下的版本
= 第一个问题: 服务号需要从8000改为7999，不然在HCU中跟已有服务冲突，MFUN待确定
= 考虑放开CV2/TensorFlow关闭部分的功能


//=ZJL, 2018 Sep.3, CURRENT_SW_DELIVERY R1.38 =>HST
= Surpress Vision + Sensor, as MATE system not solve CV2 and TensorFlow installation issue.


//=LZH, 2018 June.22, CURRENT_SW_DELIVERY R1.37 =>DjoSiteDba
= 增加后台F1sym - F11Faam Django Dba App

//=ZJL, 2018 June.9, CURRENT_SW_DELIVERY R1.36 =>RelayTest
= 增加Raspy Relay Test项目工程


//=ZJL, 2018 June.7, CURRENT_SW_DELIVERY R1.35 =>HST PRINTER
= 提供MAC地址读取服务
= 将服务号重新进行了编码，改为10进制，简化UT TEST CASE中有关十进制和16进制之间的转换，防止错误

//=ZJL, 2018 MAY.18, CURRENT_SW_DELIVERY R1.34 =>CEBS
= 继续

//=ZJL, 2018 MAY.17, CURRENT_SW_DELIVERY R1.33 =>CEBS
=生成双页面

//=ZJL, 2018 MAY.16, CURRENT_SW_DELIVERY R1.32 =>CEBS
=更新巡视功能

//=ZJL, 2018 MAY.16, CURRENT_SW_DELIVERY R1.31 =>CEBS
=增加MOTO控制功能


//=ZJL, 2018 MAY.8, CURRENT_SW_DELIVERY R1.30 =>CEBS
=完善

//=ZJL, 2018 MAY.5, CURRENT_SW_DELIVERY R1.29 =>FMPT2
= pyinstaller -F -w --icon=fmpt2.ico fmpt2Main.py

//=ZJL, 2018 MAY.4, CURRENT_SW_DELIVERY R1.29 =>CEBS
= 继续完善多任务及VISION PRCECESSING FRAMEWORK

//=ZJL, 2018 MAY.2, CURRENT_SW_DELIVERY R1.28 =>CEBS
= INIT CEBS
= cd form_qt, pyuic5 -o  cebsmainform.py cebsMainform.ui,    pyuic5 -o  cebscalibform.py cebsCalibform.ui
  pyinstaller -F -w --icon=.\icon_res\cebs.ico cebsMain.py

//=ZJL, 2018 Mar.27, CURRENT_SW_DELIVERY R1.27 =>GTJY编解码接入
= RESTClient => Firefox的插件
= 测试案例： 
复杂测试: curl -X POST -i 'http://127.0.0.1:8000/' --data '{"restTag": "special", "actionId": 20482, "parFlag": 1, "parContent": {"inputBinCode": "AA11C538326217CCA301092A0C0E1C1B7E2C01640000002C010000881300000000000024CC1000CC1000000000000100002100000000000000E803000001000D0B191B7E460111176309813D0D00F401C10341BB"}}'
简单测试: curl -X POST -i 'http://127.0.0.1:8000/' --data '{"restTag": "vision","actionId": 8194,"parFlag": 1,"parContent": {"fileName":"11.JPG", "cfBase":600, "cfSmall2MidIndex":1500, "cfMid2BigIndex":2500, "cfBig2TopIndex":5000}}'
= Django运行
  python3 manage.py runserver


//=ZJL, 2018 Mar.19, CURRENT_SW_DELIVERY R1.26 =>GTJY编解码接入
= 字段保护：判定某个字段在json格式中是否存在

//=ZJL, 2018 Mar.19, CURRENT_SW_DELIVERY R1.25 =>GTJY编解码接入
【目标1】 Ubuntu MATE自动化装机，方便现场版本的生成 => 完成
	/*************************************************************************
						***** jar包使用说明  ******
	/*************************************************************************

jar包中共有2个接口，包名称为com.chnsce.zxmeter.impl.ZXNBITOMeterInterfaces。
数据解析接口：表内的数据进行解析，返回json字符串，可自动识别表具类型和上传类型，
数据编码接口：数据打包成16进制字符串，需要上位机提供表号、开关阀指令和系统时间。
/**
	 * 数据解析函数
	 * @param sRetrunCode 表端返回的数据内容
	 * @return            解析后的json字符串
	 */
	 public String decoding(String sRetrunCode){
		retrun jsonString;
	 }
	 
实例：
水表---->>{IC卡最后一次充值量=0.0, 最后一次充值量=0.0, 信号强度=41, 阀门状态=开阀, rtn=9000, 剩余量=0.0, GPRS累计充值量=0.0, 启动日期=00-00, 单价=0.0, 表号=81980052, 累积量=0.0, 累计金额=0.0, 表内运行状态= , 表内时间=2018-3-12 9:47:18, 负计数=0.0, 表类型=A8}
气表---->>{IC卡最后一次充值量=0.0, 最后一次充值量=1.67, 信号强度=37, 统计累积量=8706, 阀门状态=开阀, SIM卡号=2147483647, 报警气量=33795, 统计日期=01-09, 启动日期=00-00, GPRS累计充值量=0.0, 单价=4.2, 表号=75126617, 负计金额=0.0, 累积量=546.6, 时间=2018-3-19 8:5:35, 累计金额=1732.2, 表内运行状态= , 程序版本号=v03C1, 上传原因标志位=  磁干扰 按键, 欠压时间=2018-1-25 15:38, 剩余金额=48267.8, 累计预购量=1000.0, 统计周期=0, 表类型=CC}

	/**
	 * 表内运行状态
	 * @param status
	 * @return
	 */
	public String getMeterStatus(byte status){
		StringBuffer result=new StringBuffer();
		result.append(" ");
		if((status&0x01)==0x01){
			result.append("余量不足");
		}
		if((status&0x02)==0x02){
			result.append(" 非法卡");
		}
		if((status&0x04)==0x04){
			result.append(" 欠费");
		}
		if((status&0x08)==0x08){
			result.append(" ");
		}
		if((status&0x10)==0x10){
			result.append(" 欠压");
		} 
		if((status&0x20)==0x20){
			result.append(" 燃气泄漏");
		} 
		if((status&0x40)==0x40){
			result.append(" 写false错");
		}
		if((status&0x80)==0x80){
			result.append(" 磁干扰");
		}
		return result.toString();
	}					  
	
	
	/**
	 * 气表上传原因标志位
	 * @return
	 */
	public String getUploadReason(byte[] status){
		StringBuffer result = new StringBuffer();
		result.append(" ");
		if((status[0]&0x01)==0x01){
			result.append("负计数");
		}
		if((status[0]&0x02)==0x02){
			result.append(" 磁干扰");
		}
		if((status[0]&0x04)==0x04){
			result.append(" 价格表错误");
		}
		if((status[0]&0x08)==0x08){
			result.append(" 欠压关阀");
		}
		if((status[0]&0x10)==0x10){
			result.append(" 非法卡关阀");
		} 
		if((status[0]&0x20)==0x20){
			result.append(" ");
		} 
		if((status[0]&0x40)==0x40){
			result.append(" ");
		}
		if((status[0]&0x80)==0x80){
			result.append(" 价格点变化");
		}
		
		if((status[0]&0x01)==0x01){
			result.append(" 插用户卡");
		}
		if((status[0]&0x02)==0x02){
			result.append(" 按键");
		}
		if((status[0]&0x04)==0x04){
			result.append(" 异常流量");
		}
		if((status[0]&0x08)==0x08){
			result.append(" 泄漏报警");
		}
		if((status[0]&0x10)==0x10){
			result.append(" 预存量卡上传");
		} 
		if((status[0]&0x20)==0x20){
			result.append(" 转入卡上传");
		} 
		if((status[0]&0x40)==0x40){
			result.append(" 转出卡上传");
		}
		if((status[0]&0x80)==0x80){
			result.append(" 余量不足");
		}
		return result.toString();
	}
					  
/**
	 * 数据编码
	 * @param barcode   表号/生产号  8位表号
	 * @param valvePar  阀门控制参数 0 ：开阀 1 ；关阀
	 * @param datetime  系统时间 格式为yyyymmddhhmmss 如20180314133829
	 * @return          16进制字符串
	 */
	public String encoding(String barcode,int valvePar,String datetime) {
		return cmdSend;
	}
实例：
水表----->>FF11338198005200001214031820000200000000000000000000000000000000000000000000000000000000000011BB
气表----->>和水表内容一致





//=ZJL, 2018 Mar.14, CURRENT_SW_DELIVERY R1.24 =>GTJY编解码接入
= JAR包使用说明
	/*************************************************************************
						***** jar包使用说明  ******
	/*************************************************************************

jar包中共有2个接口，包名称为com.chnsce.zxmeter.impl.ZXNBITOMeterInterfaces。
数据解析接口：表内的数据进行解析，返回json字符串，可自动识别表具类型和上传类型，
数据编码接口：数据打包成16进制字符串，需要上位机提供表号、开关阀指令和系统时间。
/**
	 * 数据解析函数
	 * @param sRetrunCode 表端返回的数据内容
	 * @return            解析后的json字符串
	 */
	 public String decoding(String sRetrunCode){
		retrun jsonString;
	 }
/**
	 * 数据编码
	 * @param barcode   表号/生产号 - 必须8位长度
	 * @param valvePar  阀门控制参数 0 ：开阀 1 ；关阀
	 * @param datetime  系统时间 格式为yyyymmddhhmmss 如20180314133829
	 * @return          16进制字符串
	 */
	public String encoding(String barcode, int valvePar, String datetime) {
		return cmdSend;
	}	

//=ZJL, 2018 Mar.14, CURRENT_SW_DELIVERY R1.23 =>Django命令
= 增加CCL/FAAM数据库表单

//=ZJL, 2018 Mar.11, CURRENT_SW_DELIVERY R1.22 =>Django命令
$ python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python3 manage.py migrate TestModel   # 创建表结构
注意centos下的数据库操作中，数据库密码是bxxhbxxh,而不是本地的123456。未来可以将这个改为自动shell脚本，自动更新，或者在本地发布正式代码时改好，再上传到后台云。
= Django下的密码设置，可以做到自动化

//=ZJL, 2018 Mar.2, CURRENT_SW_DELIVERY R1.21 =>PkgHstSpecial
= To GTJY request on water meter decoding
= POST的工作方式：启动服务器 python3 hstMain.py
= 另外一段客户端使用的方式:json中的数据，不能使用16机制，必须10进制
	[v]curl -X POST -i 'http://127.0.0.1:8000/' --data '{"restTag": "special", "actionId": 20481, "parFlag": 1, "parContent": {"produceNo": "11", "commandNo": "12", "htcs": "AAAA: 33", "meterTypeCode": 168}}'
	[x]curl -X POST -i 'http://127.0.0.1:8000/' --data '{"restTag": "special", "actionId": 0x5001, "parFlag": 1, "parContent": {"produceNo": "11", "commandNo": "12", "htcs": "AAAA: 33", "meterTypeCode": 0xA8}}'
= 样例
==========================
root@ubuntu:/home/hitpony# curl -X POST -i 'http://127.0.0.1:8000/' --data '{"restTag": "special", "actionId": 20481, "parFlag": 1, "parContent": {"produceNo": "11", "commandNo": "12", "htcs": "AAAA: 33", "meterTypeCode": 168}}'
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.6.4
Date: Sat, 10 Mar 2018 15:17:12 GMT
Content-type: text/html

{"restTag": "special", "actionId": 20481, "parFlag": 1, "parContent": "{\"\u9600\u95e8\u72b6\u6001\":\"\u5f00\u9600\",\"SIM\u5361\u4e32\u53f7\":\"460111176309813D0D00\",\"\u6e29\u538b\u72b6\u6001\u6807\u5fd7\u4f4d\":\"1\",\"\u5355\u4ef7\":\"3\",\"\u8868\u7c7b\u578b\u4ee3\u7801\":\"CC\",\"\u7535\u6c60\u6b20\u538b\u68c0\u6d4b1\u6b20\u538b\u65f6\u95f4\":\"2017-11-25 11:13:00\",\"\u6807\u51b5\u77ac\u65f6\u6d41\u91cf\":\"0\",\"\u5269\u4f59\u91d1\u989d\":\"50\",\"\u538b\u529b\u503c\":\"0\",\"\u6e29\u5ea6\u503c\":\"23\",\"\u8868\u5185\u8fd0\u884c\u72b6\u6001\":\"1\",\"HIC\u8fd0\u884c\u72b6\u6001\":\"0\",\"\u7d2f\u8ba1\u91cf\":\"1\",\"\u8868\u5185\u65f6\u95f4\":\"2017-11-25 11:13:00\",\"\u7edf\u8ba1\u5468\u671f\":\"0\",\"\u7d2f\u8ba1\u9884\u8d2d\u91cf\":\"0\",\"\u7edf\u8ba1\u7d2f\u8ba1\u91cf\":\"1\",\"\u6761\u7801\u53f7\":\"17623238\",\"\u4e0a\u4f20\u539f\u56e0\u6807\u5fd7\u4f4d\":\"\u4e3b\u52a8\u4e0a\u4f20\",\"\u89e3\u6790\u547d\u4ee4\":\"\u4e3b\u52a8\u4e0a\u4f20\",\"\u8d1f\u8ba1\u6570\":\"0\",\"IC\u5361\u6700\u8fd1\u4e00\u6b21\u5145\u503c\u91cf\":\"0\",\"\u4fe1\u53f7\u5f3a\u5ea6\":\"24\",\"\u4f53\u79ef\u8865\u507f\u7cfb\u6570\":\"1\",\"\u5de5\u51b5\u77ac\u65f6\u6d41\u91cf\":\"0\",\"\u7d2f\u8ba1\u91d1\u989d\":\"3\",\"\u7edf\u8ba1\u65e5\u671f\":\"09-01\",\"\u542f\u7528\u65e5\u671f\":\"00-00\",\"\u4e0a\u4f20\u65f6\u95f4\":\"2017-11-25 11:13:00\",\"\u5de5\u51b5\u7d2f\u8ba1\u91cf\":\"0\"}"}root@ubuntu:/home/hitpony# 
=============================


//=ZJL, 2018 Mar.2, CURRENT_SW_DELIVERY R1.20 =>Fmpt
= Validate jpype working method, to call JAVA JAR package

//=ZJL, 2018 Mar.2, CURRENT_SW_DELIVERY R1.19 =>Fmpt
= 建立起NAS备份目录
= 清理掉了老旧Xhat目录，未来不再使用了
= 新的目录结构
	DjoSiteDba => Django数据库框架
	env        => 安装环境说明
	fmpt       => c#的工厂生产工具
	fmpt2      => python的工厂生产工具，互联网版本
	hst        => HUIRST微服务框架应用
	NAS_tftpd  => NAS装机服务
	NAS_www    => NAS装机服务
	XfaamPrinter => FAAM打印机服务程序
	Xhhomepage => 小慧homepage服务

//=ZJL, 2018 Feb.25, CURRENT_SW_DELIVERY R1.18 =>Fmpt
= 搭建框架

//=ZJL, 2018 Feb.23, CURRENT_SW_DELIVERY R1.17 =>Django
= HUIREST API性能评估
  -> HUIREST的压测性能评估很有意思：使用HTTP/POST远程API CURL方式访问数据库，连续做100个循环，每个循环有4个Test Case，分别为数据表单的插入，删除，插入，修改。结果从UT环境中来看，100个HTTP REQUEST在2ms之内，全部发送到服务器侧，但回复却是在接下来的4s内一个一个的返回来的。
  -> 这给了我们两个有意思的启示：1）Python3和HUIREST API是异步的，并不是同步的，意味着它不等返回结果，就去执行下面的语句，所以在我们的业务处理中要仔细处理这个内容。 2)400个表单操作API耗时4s，PPS=100，差不多每一次数据库操作在10ms水平，在对于业务应用模块来说，这是相当慢的，这也说明HUIREST API只能当做一种外部硬盘一样的慢速介质，而不能支持特别高速的业务实时应用
  -> 满负荷跑的时候，CPU才10%左右，这台机器有8个核吧，所以只有一个核在跑，我估计
  -> http://blog.csdn.net/AnyThingFromBigban/article/details/73611386
  -> 如果想使用多核，需要使用MultiProcessing处理机制，或者Ctypes外部c/c++扩展模块，绕过Python的GIL全局锁，才能将多核用足。对于系统全局来说，应用业务跑在一个核上，不同的微服务（HUIREST API）跑在另外的核上，界面再跑在其他核上，他们都是独立的进程，操作系统自然将他们调度在不同的核上，这个就自然不是问题了
  -> 从这儿可以看出，对于数据库IO密集型的访问来说，Python的确不是最优方案，业界广泛使用Java Hibernate / MyBatis框架是有道理的，但对我们来说，是不是足够了，需要再评估一下
  -> 按照扬尘业务1分钟汇报一次的话务强度，每一次话务呼叫，我们假设有4次数据库操作，这样一个云后台的单核，可以支持的终端数量 = 1/ ((1/60) * 0.01*4) = 60*100/4 = 1500，即我们的一个业务后台，可以支持1500个下位机终端，无论上云控锁还是扬尘系统，这已经足够优秀了
  -> 云控锁的话务密度为8个小时一次呼叫，所以这根本不会成为瓶颈。
  -> 有了这个SYSTEM DIMENSIONING之后，我们在确定软硬件架构方面，就有底气了。同时，遇到后台的性能瓶颈，我们也能知道优化的方向和维度了。  
  
//=ZJL, 2018 Feb.20, CURRENT_SW_DELIVERY R1.16 =>Django
= CONN_MAX_AGE参数的设置不能放在OPTION里面，而必须放在跟NAME/HOST并行的外部
= 创建CEBS项目APP内容
= 创建COMM项目APP内容，并建立了基础的数据表单，实验数据表单的操作以及对应的ＵＴ工作环境
= 随时执行python3 manage.py dumpdata DappDbComm > DappDbComm.json，对数据进行备份
= 搭建起基本的CEBS线虫项目数据库访问机制，可以实现User，用户提交以及识别的访问．要搭建整个线虫项目，还需要考虑如何设计界面问题
= 完成Cebs项目中所有的UT TEST CASES

//=ZJL, 2018 Feb.19, CURRENT_SW_DELIVERY R1.15 =>Django
= 为了实现DjoSiteDba和hst的共享，并实现当前的hst访问DjoSiteDba的外部访问，同事让Django的运行不受影响，绕过的坑有：
 -> http://localhost:8001/user_info_show/ 使用8001端口，访问Django的路由
 -> 将DjoSiteDba目录放在hst目录之内，跟hst目录保持平行，而不是放在里面
 -> 在外部项目hst中，使用sys.path.append('../DjoSiteDba/'), django.setup(), 从而访问from DappDbTest import views as DappDbTest_views
 -> 8001可以不启动，不影响hst的运行
 -> 参数request必须传进去给view．目前request格式就是json，已经在httpCmd中被解析了，所以内部使用还是很方便的
 -> UT的执行，采用RUN AS方式
 -> 在Eclipse工程里面，使用外部独立的项目DjoSiteDba，从而让其能够使用Eclipse集成的Django功能模块，不然就需要在外部Linux Terminal中敲入每一个独立的命令
 -> UT的输入参数，采用标准的Json结构，将所有的参数全部放在Par中，方便解析与使用．这种方式将跟标准的使用保持同步．
 -> 严格维持了HUIREST的POST方式，并验证了POST方式工作的可行性与严谨性
= CONN_MAX_AGE：缓冲池设置为无限长

//=ZJL, 2018 Feb.19, CURRENT_SW_DELIVERY R1.14 =>Django
= 搞定初步的Django项目安排：将项目内容建立在sdde/hst目录下，但项目建立在外部，独立成为一个项目：DjoSiteDba
= 需要在sdde/hst/DjoSiteDba/目录下运行　python3 manage.py runserver 127.0.0.1:8001．未来是否使用8001或者8000端口，再定
= 同步需要启动python3 hstEntry.py，在8000端口，这是基础的hst服务．这样，两个服务同步启动．
  此时，启动8001端口，只是为了方便验证并获取数据库操作的结果．其实，从PhpMyAdmin中，也能很方便的得知结果，所以启动8001/runserver不是必须的
  这种模式就非常好：只需要启动8000这个服务端口，复用了Django的ORM数据库访问功能，而根本不需要Django的路由功能，这就是我们所追求的！

//=ZJL, 2018 Feb.17, CURRENT_SW_DELIVERY R1.13 =>Django
= 重复多遍之后，确定可以重复安装的方法，放在InsGuidance.txt文件中
= 安装成功Django=2.1.0最新版本

//=ZJL, 2018 Feb.10, CURRENT_SW_DELIVERY R1.12 =>年后目标
有关装机的过程，综合之前的过程，有如下几个地方需要优化一下：
1）装机到一半，没有执行到100% 
2）中文输入法的自动安装 
3）WIFI网络的自动配置 
4）Tomcat7 + SpringMVC + Herbinet安装环境 
5)一旦装机完成，需要将服务器映射到外网服务器，以便未来安装更多的服务组件，或者可以在xiaohui服务器之间灵活切换 
6）安装脚本备份到SDDE VOB中 
7）hcu.sh脚本和服务的自动启动  
8）ubuntu MATE环境是完整的吧？年后可能需要批量安装10套以上。
9) Eclipse的Php/Java/Cpp/Js开发环境，全部安装到位

//=ZJL, 2018 Jan.15, CURRENT_SW_DELIVERY R1.11 =>JSON-C库
= Mosca的安装方法
= Json-C在AdvanceTech上的安装方法


//=ZJL, 2017 Dec.27, CURRENT_SW_DELIVERY R1.10 =>HUIREST
= 搭建AITEST以及相应RESTFUL API的模块框架

//=ZJL, 2017 Dec.23, CURRENT_SW_DELIVERY R1.09 =>HUIREST
= 将SDDE部署到NX
= 增加网络部署逻辑图
= 将U17装机宝典放入SDDE环境

//=ZJL, 2017 Dec.17, CURRENT_SW_DELIVERY R1.08 =>HUIREST
= 完善VISION中线虫识别功能，成功改造为HUIRST服务

//=ZJL, 2017 Dec.15, CURRENT_SW_DELIVERY R1.07 =>HUIREST
= 创建图形处理的工具
= 完善BillTool用来处于apple的图象差异
= 搞定了线虫的处理，未来可以将其部署到服务器进行具体的应用

//=ZJL, 2017 Dec.11, CURRENT_SW_DELIVERY R1.06 =>HUIREST
= 将所有的组件库分离，重新定义入口
= 增加UT功能，建立TestSuit集合框架
= python3.6 hstEntry, Eclipse中进行UT的测试，从而同时跑服务器和客户端
= 安装了大量的urllib3/pyurl等组件，终于将http的客户端跑起来了

//=ZJL, 2017 Dec.11, CURRENT_SW_DELIVERY R1.05 =>HUIREST
= 创建HUIREST的Python程序框架
= 基本上完成了HUIREST的功能构建，它可以兼容PRINT/DBA/VISION

=> http://blog.csdn.net/linda1000/article/details/8087546
	BaseHTTPRequestHandler其中的实例变量有：
	1）client_address 包含关联的客户端地址（host, port）
	2）command 包含请求类型（eg: get ）
	3）path 包含的请求路径
	4）request_version 包含请求版本的字符串（eg: 'HTTP/1.0'）
	5）headers
	6）rfile 输入流
	7）wfile 包含写到客户端响应的输出流
	BaseHTTPRequestHandler的类变量有：
	1）server_version 指定服务器软件版本
	2）sys_version Python系统版本
	3）error_message_format
	4）protocol_version 响应中使用的HTTP协议版本
	BaseHTTPRequestHandler部分操作
	1）handle()
	2）send_error(code[, message]) 发送并记录一个完整的错误回复到客户端
	3）send_response(code[, message]) 发送一个响应头并记录已接收的请求
	4）send_header(keyword, value) 编写一个指定的HTTP头到输出流
	5）version_string() 饭后服务器软件的版本字符串
=> HTTP测试界面
	moz-extension://3ab3f452-9583-4d81-bfdb-230f641710ce/index.html#
	{
	    "restTag": "vision",
	    "actionId": 8193,
	    "parFlag": 1,
	    "parContent": {
	        "sn": 55,
	        "sucFlag": 1,
	        "errCode": 0
	    }
	}
	
//=MYC, 2017 Dec.8, CURRENT_SW_DELIVERY R1.04 =>创建整个环境
= FMPT工具，将相关源代码纳入管理

//=LZH, 2017 Dec.3, CURRENT_SW_DELIVERY R1.03 =>创建整个环境
= 增加XH网站代码

//=ZJL, 2017 Nov.22, CURRENT_SW_DELIVERY R1.02 =>创建整个环境
= 创建不同分支
= 创建Gpp（General Purpose）通用脚本目录
= 创建Raspy分支

//=QL, 2017 Nov.22, CURRENT_SW_DELIVERY R1.01 =>xxx
= 创建整个SDDE VOB环境


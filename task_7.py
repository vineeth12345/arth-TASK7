import os
import getpass
print("""
Press 1. Integrate Lvm With Hadoop
press 2. to resize the Lvm
press 3. to setup lvm
press 4. to configure webserver and 
press 5. run python code inside container""")
ask=int(input("enter your choice"))

if ask==1:
	ask2=int(input("How Many Nodes You Have"))
	hyt=[]	
	pyt=[]
	for k in range(0,ask2):
		if k==0:
			ask31=input("Enter the Ip of NameNode")
			hyt.append(ask31)
			passs=getpass.getpass("enter your password")
			pyt.append(passs)
	
		elif k==1:
			ask31=input("Enter the Ip of Client")
			hyt.append(ask31)
			passs=getpass.getpass("enter your password")
			pyt.append(passs)
		elif k>1:
			ask31=input("Enter the Ip of DataNode".format(k-1))
			hyt.append(ask31)
			passs=getpass.getpass("enter your password")
			pyt.append(passs)
			
		
	for i in range(0,ask2):		
		if i==0:
			ask31=hyt[i]
			passs=pyt[i]
			a = 'ssh {} yum install sshpass -y'.format(ask31)
			os.system(a)
			
		
			a="""sshpass -p {} ssh {} wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://ram111111.s3.amazonaws.com/software/hadoop-1.2.1-1.x86_64.rpm""".format(passs,ask31)
			os.system(a)

			a="""sshpass -p {} ssh {} wget -O /root/jdk-8u171-linux-x64.rpm https://ram111111.s3.amazonaws.com/software/jdk-8u171-linux-x64.rpm""".format(passs,ask31)
			os.system(a)

			a = 'sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(passs,ask31)
			print(os.system(a))
			a='sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(passs,ask31)
			print(os.system(a))	


			a="""sshpass -p {} ssh {} wget -O /etc/hadoop/core-site.xml https://ram111111.s3.amazonaws.com/namenode/core-site.xml""".format(passs,ask31)
			os.system(a)

			a="""sshpass -p {} ssh {} wget -O /etc/hadoop/hdfs-site.xml https://ram111111.s3.amazonaws.com/namenode/hdfs-site.xml""".format(passs,ask31)				
			os.system(a)

			a="""sshpass -p {} ssh {} systemctl stop firewalld""".format(passs,ask31)
			os.system(a)
			a='sshpass -p {} ssh {} systemctl disable firewalld'.format(passs,ask31)
			os.system(a)		
			a='sshpass -p {} ssh {} hadoop namenode -format'.format(passs,ask31)
			os.system(a)
			a='sshpass -p {} ssh {} hadoop-daemon.sh start namenode'.format(passs,ask31)
			os.system(a)
		elif i==1:
			ask3=hyt[i]
			passs=pyt[i]
			a="""sshpass -p {} ssh {} wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://ram111111.s3.amazonaws.com/software/hadoop-1.2.1-1.x86_64.rpm""".format(passs,ask3)
			os.system(a)

			a="""sshpass -p {} ssh {} wget -O /root/jdk-8u171-linux-x64.rpm https://ram111111.s3.amazonaws.com/software/jdk-8u171-linux-x64.rpm""".format(passs,ask3)
			os.system(a)

			a = 'sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(passs,ask3)
			print(os.system(a))
			a='sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(passs,ask3)
			print(os.system(a))	
			
			a="""wget -O /core-site.xml https://ram111111.s3.amazonaws.com/namenode/core-site.xml"""
			os.system(a)

			with open('/core-site.xml') as f:
    				newText=f.read().replace('0.0.0.0', ask31)

			with open('/core-site.xml', "w") as f:
    				f.write(newText)
			os.system('sshpass -p {} scp /core-site.xml {}:/etc/hadoop/core-site.xml'.format(passs,ask3))




		elif i>1:
			ask3=hyt[i]
			passs=pyt[i]
			print("""press 1 to list devices you have
press 2 to continue""")
			gg=int(input("enter value"))
			count=int(input("how many devices you have"))
			
			hh='sshpass -p {} ssh {} fdisk -l'.format(passs,ask3)
			if gg==1:
				print(os.system(hh))
			elif gg==2:
				pass
			xg=[]
			d = """"""
			for i in range(0,count):
				device=input("enter the device{} name".format(i+1))
				xg.append(device)
				d=d+' '+xg[i]

				a = 'sshpass -p {} ssh {} pvcreate {}'.format(passs,ask3,device)
				print(os.system(a))		

			name = input("enter you vg name")

			c = 'sshpass -p {} ssh {} vgcreate {} '+d
			c = c.format(passs,ask3,name)
			print(os.system(c))

			partname=input("enter the partition name")
			size1 = input("enter the size you want")

			d = 'sshpass -p {} ssh {} lvcreate {} --size {} --name {} -y'.format(passs,ask3,name,size1,partname)
			print(os.system(d))

			e='sshpass -p {} ssh {} mkfs.ext4 /dev/'+name+'/'+partname
			e=e.format(passs,ask3)
			f='sshpass -p {} ssh {} mount /dev/'+name+'/'+partname+' /data'
			f=f.format(passs,ask3)			
			print(os.system(e))
			g='sshpass -p {} ssh {} mkdir /data'.format(passs,ask3)
			os.system(g)
			os.system(f)		
			

			a="""sshpass -p {} ssh {} wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://ram111111.s3.amazonaws.com/software/hadoop-1.2.1-1.x86_64.rpm""".format(passs,ask3)
			os.system(a)

			a="""sshpass -p {} ssh {} wget -O /root/jdk-8u171-linux-x64.rpm https://ram111111.s3.amazonaws.com/software/jdk-8u171-linux-x64.rpm""".format(passs,ask3)
			os.system(a)			

			a = 'sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(passs,ask3)
			print(os.system(a))
			a='sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(passs,ask3)
			print(os.system(a))	


			a="""wget -O /core-site.xml https://ram111111.s3.amazonaws.com/namenode/core-site.xml"""
			os.system(a)

			a="""sshpass -p {} ssh {} wget -O /etc/hadoop/hdfs-site.xml https://ram111111.s3.amazonaws.com/datanode/hdfs-site.xml""".format(passs,ask3)				
			os.system(a)

			with open('/core-site.xml') as f:
    				newText=f.read().replace('0.0.0.0', ask31)

			with open('/core-site.xml', "w") as f:
    				f.write(newText)
			os.system('sshpass -p {} scp /core-site.xml {}:/etc/hadoop/core-site.xml'.format(passs,ask3))
			os.system('sshpass -p {} ssh {} systemctl stop firewalld'.format(passs,ask3))
			os.system('sshpass -p {} ssh {} systemctl disable firewalld'.format(passs,ask3))		
			os.system('sshpass -p {} ssh {} hadoop-daemon.sh start datanode'.format(passs,ask3))

elif ask==2:

	print("""
	press 1: to increase
	press 2: to decrease""")
	ask22=int(input("enter your choice"))	
	if ask22==1:
		ask23=input("enter the lvm name which you want to increase")
		ask24=input("enter the size you want to increase")
		a='lvextend --resizefs --size +{} {}'.format(ask24,ask23)			
		os.system(a)

	elif ask22==2:
		ask23=input("enter the lvm name which you want to decrease")
		ask24=input("enter the final size of partition")
		a='lvreduce --resizefs --size {} {} -y'.format(ask24,ask23)			
		os.system(a)
	
elif ask==3:

	count=int(input("how many devices you have for the vg"))

	xg=[]
	d = """"""
	for i in range(0,count):
		print(os.system('fdisk -l'))
		device=input("enter the device{} name".format(i+1))
		xg.append(device)
		d=d+' '+xg[i]

		a = 'pvcreate {}'.format(device)
		print(os.system(a))

	name = input("enter you vg name")

	c = 'vgcreate {} '+d
	c = c.format(name)
	print(os.system(c))

	partname=input("enter the partition name")
	size1 = input("enter the size you want")

	d = 'lvcreate {} --size {} --name {} -y'.format(name,size1,partname)
	print(os.system(d))

	e='mkfs.ext4 /dev/'+name+'/'+partname

	print(os.system(e))
	mo = input("enter the folderpath to which you want to mount")
	tomy = 'mkdir '+mo
	os.system(tomy)
	gght='mount /dev/'+name+'/'+partname+' '+mo
	os.system(gght)

elif ask==4:	
	os.system('systemctl start docker')
	os.system('docker create -it --name rohan_webserver ubuntu')
	os.system('docker start rohan_webserver')
	os.system('docker exec -it rohan_webserver apt-get update')
	os.system('docker exec -it rohan_webserver apt-get install apache2 -y')
	os.system('docker exec -it rohan_webserver apt-get install wget')
	os.system('docker exec -it rohan_webserver apt-get install net-tools')
	os.system('docker exec -it rohan_webserver wget -O /var/www/html/index.html https://ram111111.s3.amazonaws.com/index.html')
	os.system('docker exec -it rohan_webserver service apache2 start')
	os.system('docker exec -it rohan_webserver ifconfig eth0')

elif ask==5:
	os.system('systemctl start docker')
	os.system('docker create -it --name rohan_python ubuntu')
	os.system('docker start rohan_python')
	os.system('docker exec -it rohan_python apt-get update')
	os.system('docker exec -it rohan_python apt-get install python3 -y')
	os.system('docker exec -it rohan_python apt-get install wget')
	os.system('docker exec -it rohan_python wget -O /salary.py https://ram111111.s3.amazonaws.com/salary.py')
	os.system('docker exec -it rohan_python wget -O /SalaryData.csv https://ram111111.s3.amazonaws.com/SalaryData.csv')
	os.system('docker exec -it rohan_python apt-get install python3-pip -y')
	os.system('docker exec -it rohan_python pip3 install sklearn')
	os.system('docker exec -it rohan_python pip3 install pandas')
	os.system('docker exec -it rohan_python python3 /salary.py')
		
		















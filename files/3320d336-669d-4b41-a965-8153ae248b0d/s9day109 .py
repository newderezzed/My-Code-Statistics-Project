s9day109 

内容回顾：
	1. git的作用？
	
	2. git命令？
		git init 
		git add 
		git status 
		git commit 
		git log 
		git reflog 
		git reset --hard
		git checkout 
	
	3. 路飞表结构：
		- 课程（13表）
			- 课程大类
			- 课程子类
			- 学位课
				- 讲师
				- 奖学金
			- 专题课（学位课模块表）
			- 价格策略(contenttype)
			- 课程详细(o2o -> 水平分表)
			- 常见问题
			- 课程大纲
			- 章节
			- 课时
			- 作业 
		- 深科技（4+2）
			- 用户表
			- 用户token
			- 文章来源
			- 文章表
			- 通用评论表
			- 通用收藏表
			
	4. 谈谈你对 django rest framework框架的认识？
		- 路由， 
			- 可以通过as_view传参数，根据请求方式不同执行相应的方法
			- 可以在url中设置一个结尾，类似于： .json 
		- 视图，
			- 帮助开发者提供了一些类，并在类中提供了多个方法以供我们使用。
		
		- 版本，
			- 在url中设置version参数，用户请求时候传入参数。在request.version中获取版本，根据版本不同做不同处理
		
		- 认证，
			-  写一个类并注册到认证类，在类的的authticate方法中编写认证逻辑。
				- 认证成功（user,auth）
				- raise AuthticateFaild(....)
				- None 
		- 权限
			-  写一个类并注册到权限类，在类的的has_permission方法中编写认证逻辑。
				- True 
				- False 
		
		- 频率限制
			-  写一个类并注册到频率类，在类的的 allow_request/wait 方法中编写认证逻辑。
				
				allow_request
					- True 
					- False  如果返回False，那么就要执行wait
					
		- 解析器，
			- 根据ContentType请求头，选择不同解析器对 请求体中的数据进行解析。
			
				POST /index/ http1.1.\r\nhost:11.11.11.11\r\nContent-Type:url-formendo.... \r\n\r\nuser=alex&age=123
				POST /index/ http1.1.\r\nhost:11.11.11.11\r\nContent-Type:application/json\r\n\r\n{....}
			
		- 分页 
			- 对从数据库中获取到的数据进行分页处理: SQL -> limit offset 
				- 根据页码：http://www.luffycity.com/api/v1/student/?page=1&size=10
				- 根据索引：http://www.luffycity.com/api/v1/student/?offset=60&limit=10
				- 根据加密：http://www.luffycity.com/api/v1/student/?page=erd8
				
			赠送：页码越大速度越慢，为什么以及如何解决？
				  原因：页码越大向后需要扫描的行数越多，因为每次都是从0开始扫描。
				  解决：
						- 限制显示的页数
						- 记录当前页数据ID最大值和最小值，再次分页时，根据ID现行筛选，然后再分页。
						
		- 序列化  
			- 对queryset序列化以及对请求数据格式校验。
			
		- 渲染器
			- 根据URL中传入的后缀，决定在数据如何渲染到到页面上。
				
今日内容：
	- git 
	- redis
	
内容详细：
	1. git，小东北创业史。
	
		第一阶段：在沙河的日子
			
	
		第二阶段：开发直播功能，开发过程中临时需要修复bug或临时新功能到来。
		
			方式一：
				git stash 
				git stash pop 
				
				git stash           将当前工作区所有修改过的内容存储到“某个地方”，将工作区还原到当前版本未修改过的状态
				git stash list      查看“某个地方”存储的所有记录
				git stash clear     清空“某个地方”
				git stash pop       将第一个记录从“某个地方”重新拿到工作区（可能有冲突）
				git stash apply     编号, 将指定编号记录从“某个地方”重新拿到工作区（可能有冲突） 
				git stash drop      编号，删除指定编号的记录
			
				git stash作用，帮助我们暂时存储已经开发一些功能的代码，继续做其他事情，做完之后，再回来继续开发
			方式二：
				git branch 
				git branch dev      
				git branch bug       
				git branch -d bug 
				git checkout dev 
				git merge bug       
				
				
			面试题：如果代码出现bug，你们是如何解决？
					创建一个bug分支，然后进行bug处理，处理完毕后，合并到master分支。
					删除bug分支
					回到dev分支继续开发。
					
					
		第三阶段：在三里屯买了一层楼。
				  需要一个代码托管的网站：github、Bitbucket、码云
				  自己创建代码托管的网站：gitlab 
				
				  注册账号：
						用户名：邮箱
						密码：admin123
					
				命令：
					git remote add origin .........
					
					
					git push origin dev 
					git clone https://github.com/WuPeiqi/dbhot.git
					git pull origin dev 
						git fetch origin dev 
						git merge origin/dev   改：  git rebase origin/dev 
					git pull origin master 
						git fetch origin master
						git merge origin/master
					
	
				面试题： git rebase的作用？
					     保持提交记录的整洁。
					
	
	2. redis 
		mysql是一个软件，帮助开发者对一台机器的硬盘进行操作。
		redis是一个软件，帮助开发者对一台机器的内存进行操作。
		
		
		关键字：
			缓存，优先去redis中获取，如果没有就是数据库。
			
			
		安装：
			- redis软件
				- yum install redis 
					redis-server /etc/redis.conf 
				- 
					wget http://download.redis.io/releases/redis-3.0.6.tar.gz
					tar xzf redis-3.0.6.tar.gz
					cd redis-3.0.6
					make
					
					/src/redis-server redis.conf 
					
					
					默认端口：6379
				
				配置文件：
					bind 0.0.0.0
					port 6379
					requirepass dskjfsdf
					
					
			- python连接redis的模块
				
				pip3 install redis 
	
	
	
		基本使用：
			a. 
				import redis
				# 创建连接
				# conn = redis.Redis(host='47.94.172.250',port=6379,password='luffy1234')
				# conn.set('x1','wanghuaqiang',ex=5)
				# val = conn.get('x1')
				# print(val)
			b.
				# 连接池
				# import redis
				#
				# pool = redis.ConnectionPool(host='10.211.55.4', port=6379,password='luffy1234',max_connections=1000)
				# conn = redis.Redis(connection_pool=pool)
				#
				# conn.set('foo', 'Bar')

				连接池注意：连接池只创建一次
	
	
总结：
	1. git+github 
	2. redis 
	
	
	
	
	
	
	
	
	
	
	
	
	
s9day110 
内容回顾：
	1. git开发时，出bug如何结局？
	
	2. git rebase的作用？
	
	3. git 命令？
		
	4. redis是什么？
		用于操作内存的软件。
		- 可以做持久化：
			- AOF
			- RDB
		- 相当于是大字典
		
		- 单进程单线程
	
	5. 使用连接池
		本质，维护一个已经和服务端连接成功的socket。
		以后再次发送数据时，直接获取一个socket，直接send数据。
	
	6. 路飞表结果
		- 课程
			- 大类
			- 子类
			- 学位课
			- 奖学金
			- 老师
			- 专题课
			- 课程详细
			- 大纲
			- 作业
			- 章节
			- 课时
			- 价格策略
		- 深科技
			- 文章来源
			- 文章
			- 用户
			- token
			- 评论 
			- 收藏 
	7. 支付宝支付
	
		- 加密方式：rsa
		- 公钥私钥：
				- 商户私钥
				- 支付宝公钥
		- 支付成功后，断电宕机
				- 成功：return HttpResponse('success')
				
	8. rest framework框架
		
	9. 数据库页数越大速度越慢。
		- 限制页数
		- 记录当前页最大ID、最小ID
		- 错误答案：
			- 扫描索引表
			- 再去数据库表中获取数据


今日内容：
	1. git 
	2. redis
	3. 改代码
	

内容详细：
	1. git 
		第四阶段： 多人协同开发
			1. 允许他人操作程序
				- 合作者
				- 创建组织
			
			2. 分支
				- master
				- dev 
				- xdb
				- zhh
			3. 规则
				- 一起合并
				- 合并时间：1/2
			
			问题：
				$ git push origin dev
				To https://github.com/WuPeiqi/dbhot.git
				 ! [rejected]        dev -> dev (fetch first)
				error: failed to push some refs to 'https://github.com/WuPeiqi/dbhot.git'
				hint: Updates were rejected because the remote contains work that you do
				hint: not have locally. This is usually caused by another repository pushing
				hint: to the same ref. You may want to first integrate the remote changes
				hint: (e.g., 'git pull ...') before pushing again.
				hint: See the 'Note about fast-forwards' in 'git push --help' for details.
	
			4. 做代码review
				如何做代码review？
					- 创建review分支：
				谁来锁代码review？
					- 组长
					- 带你的人
			
			
		第五阶段：给别人代码贡献力量
			
			问题: 如果你要在github上给别人代码添加功能？
				  fork
				  pull request 
			
			
		
		其他：
			a. 不用反复输入用户名密码登录
				Https:
					https://用户名:密码@github.com/WuPeiqi/dbhot.git
					git remote add origin  https://用户名:密码@github.com/WuPeiqi/dbhot.git
				
				SSH:
					git@github.com:WuPeiqi/dbhot.git
			
			b. .gitignore文件 
			
			
			c. 版本 
				    git tag -a v1.0 -m '版本介绍'        本地创建Tag
					git show v1.0                       查看
					git tags -n                         查看本地Tag
					git tag -l 'v1.4.2.*'               查看本地Tag，模糊匹配
					git tag -d v1.0                     删除Tag
					git push origin :refs/tags/v0.2     更新远程tag
					git checkout v.10                   切换tag
					git fetch origin tag V1.2

					git push origin  --tags
					git pull origin  --tags
					
					
					git clone -b v1.0  https://github.com/WuPeiqi/dbhot.git
			
			
			
		要求：
			1. 组长创建项目（把自己的路飞学城api）：master/dev 
			2. 组长邀请组员尽力啊
			3. 组员：
				- 创建自己分支
				- 修改代码，去提交。
		
		组长：今天晚上发送项目地址

			
			
	2. redis 
		特点：
			a. 持久化
			b. 单进程、单线程
			c. 5大数据类型
			
				redis={
					k1:'123',  字符串
					k2:[1,2,3,4,4,2,1], 列表
					k3:{1,2,3,4}, 集合
					k4:{name:123,age:666}, 字典
					k5:{('alex',60),('eva-j',80),('rt',70),}，有序集合
				}
		使用字典：
			- 基本操作
			- 慎重使用hgetall, 优先使用 hscan_iter
			- 计数器
			
			注意事项：redis操作时，只有第一层value支持：list,dict ....
		
		
		应用（django）：
			1. 自定义使用redis
			
			2. 使用第三方组件
				pip3 install django-redis 
				
				配置：
					CACHES = {
						"default": {
							"BACKEND": "django_redis.cache.RedisCache",
							"LOCATION": "redis://127.0.0.1:6379",
							"OPTIONS": {
								"CLIENT_CLASS": "django_redis.client.DefaultClient",
								"CONNECTION_POOL_KWARGS": {"max_connections": 100}
								# "PASSWORD": "密码",
							}
						}
					}
						
				使用：
					import redis
					from django.shortcuts import render,HttpResponse
					from django_redis import get_redis_connection


					def index(request):
						conn = get_redis_connection("default")
						return HttpResponse('设置成功')
					def order(request):
						conn = get_redis_connection("back")
						return HttpResponse('获取成功')
	
	
				高级使用：
					1. 全站缓存
					
					2. 单视图
					
					3. 局部页面
	
			
			补充：rest framework框架访问频率限制推荐放到 redis/memecached
			
		
	
	
	
	
	
	
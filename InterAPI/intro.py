# 接口：提供数据交互的渠道，基于网络协议（大部分都是HTTP）进行数据传输，所有接口由服务端实现
    # HTTP协议： 网络协议://IP:Port/path?args1-xxx&args2=xxx
# 所有接口都有其指定的URL，一般有接口文档进行描述，包括URL，参数，返回值的格式和内容等
    # 下发：Request请求
    # 接受：Response响应
    # 通过下发请求——经由网络协议传输至后端接口——接口执行运算（查询、匹配、计算等）——生成响应——返回至下发端
# 接口测试：校验后端逻辑、性能测试、安全测试
# Python+Requests环境搭建
# 接口自动化实现
    # 基于reques库模拟下发请求，校验接口的正确性
        # http网络协议下，主流的请求方法有get、post（一般数据查询用get，数据更新和提交用post）

# 接口响应的状态码
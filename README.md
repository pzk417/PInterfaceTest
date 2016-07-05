# PInterfaceTest
简单的python自动化测试实现
v1.0：
设计思路
    1:从excel读取测试case
    excel设计的字段：
    Tase_name：案例名称
    Interface_name：接口名称
    Method：post/get
    URL：执行url
    Params：输入参数
    Expectation：期望值
    Result：实际结果
    Function：调用函数
    MLogin:是否需要登录(假如需要登录)
    2:用python的单元测试框架 作为runner执行
    unittest.TestSuite()
    runner.run(test_suite)
    3:生成html 实时画出一个html 表格
    htmlreport
    4:项目结构
    --project
         --model
              --testsuit
                   --testcase
                       --testdata



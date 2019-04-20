from pyhessian.client import HessianProxy


service = HessianProxy("http://hessian.caucho.com/test/test", version=2)
print(service.replyDate_1())

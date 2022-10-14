from v6 import va_core
import time
time.sleep(5)
print(va_core.VA_Core.clickUsingSearch('Elements','Themes',0,0,iter=60,relative_to_axis_by=-40))
print(va_core.VA_Core.clickUsingSearch('Elements','Media',0,0,iter=60,relative_to_axis_by=-40))
print(va_core.VA_Core.clickUsingSearch('Elements','Audio',0,0,iter=60,relative_to_axis_by=-40))
print(va_core.VA_Core.clickUsingSearch('Elements','Back',0,0,iter=60,relative_to_axis_by=-20))
# va_core.VA_Core.getTextLocation('Terminal')

import time

import day7

start = time.time()
print(day7.main())
end = time.time()
print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")

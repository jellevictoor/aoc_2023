import time

import day8

start = time.time()
print(day8.main())
end = time.time()
print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")

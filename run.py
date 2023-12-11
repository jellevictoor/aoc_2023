import time

import day11

start = time.time()
print(day11.main())
end = time.time()
print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")

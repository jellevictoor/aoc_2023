import time

import day10
import day11

start = time.time()
print(day10.main())
end = time.time()
print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")

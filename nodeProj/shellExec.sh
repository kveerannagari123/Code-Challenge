ps aux | awk '{printf("{\"PID\":%s,\"CPU\":%s},",$2,$3)}'
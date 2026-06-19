import math
import random
import time
from threading import Lock, Thread


class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate: int):
        self.max_capacity = capacity
        self.refill_rate = refill_rate
        self.users = {}
        self.lock = Lock()

    def print_user_data(self, user):
        print(
            f"\nUser: {user} | Tokens: {self.users[user]['tokens']:.2f} | Last Refill: {self.users[user]['last_refill']:.4f}")

    def allow_request(self, user: str) -> bool:
        current_time = time.time()

        with self.lock:
            if user not in self.users:
                self.users[user] = {
                    "tokens": self.max_capacity,
                    "last_refill": current_time
                }
            user_data = self.users[user]

            elapsed_time = current_time - user_data["last_refill"]
            added_tokens = math.floor(elapsed_time * self.refill_rate)

            if added_tokens > 0:
                user_data["tokens"] = min(self.max_capacity, added_tokens + user_data["tokens"])
                user_data["last_refill"] = current_time

            self.print_user_data(user)
            if user_data["tokens"] >= 1:
                user_data["tokens"] -= 1
                return True
            return False


# rate_limiter = TokenBucketRateLimiter(2, 1)
# for tries in range(50):
#     print("============================================================")
#     print(f"{"Allowed" if rate_limiter.allow_request("amar") == True else "Denied"}")
#     wait_time = random.randint(0, 2)
#     print(f"Waiting for {wait_time}")
#     time.sleep(wait_time)


def worker(rate_limiter, user, thread_id):
    for i in range(10):
        allowed = rate_limiter.allow_request(user)
        print(f"[Thread {thread_id}] Request {i}: {'Allowed' if allowed else 'Denied'}")
        wait_time = random.randint(0, 2)
        print(f"[Thread {thread_id}] Waiting for {wait_time}")
        time.sleep(wait_time)


rate_limiter = TokenBucketRateLimiter(capacity=2, refill_rate=1)
threads = []

# Spawn 4 concurrent threads hitting the same user "amar"
for i in range(4):
    t = Thread(target=worker, args=(rate_limiter, "amar", i))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
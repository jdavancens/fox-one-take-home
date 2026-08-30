class Logger:

    def __init__(self):
        self.logs: list[str] = []

    def log(self, message: str) -> None:
        self.logs.append(message)

    def get_logs(self) -> list[str]:
        return [*self.logs]

    def search(self, query: str) -> list[str]:
        results = []
        for log in self.logs:
            if query in log:
                results.append(log)
        return results
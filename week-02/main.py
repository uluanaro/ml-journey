"""Демо-запуск анализатора данных."""
from analysis import ReportAnalyzer

if __name__ == "__main__":
    numbers = [12, 7, 23, 7, 42, 15, 8, 23, 7, 30]
    words = ["Python", "ml", "python ", "Data", "ML", "data", "python", "AI"]

    analyzer = ReportAnalyzer(numbers, words)
    print(analyzer)
    print(analyzer.number_stats())
    print(analyzer.word_stats())
    print(analyzer.text_report())
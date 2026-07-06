"""Классы для анализа числовых и текстовых данных."""


class DataAnalyzer:
    """Хранит числа и слова, считает по ним базовую статистику."""

    def __init__(self, numbers, words):
        self.numbers = numbers
        self.words = words

    def number_stats(self):
        """Возвращает min/max/avg/sum по числам или None, если данных нет."""
        if not self.numbers:
            return None
        number = len(self.numbers)
        return {
            "min": min(self.numbers),
            "max": max(self.numbers),
            "avg": sum(self.numbers) / number,
            "sum": sum(self.numbers),
        }

    def word_stats(self):
        """Возвращает частоты, уникальные и самое частое слово или None."""
        if not self.words:
            return None
        new_words = [w.strip().lower() for w in self.words]
        counts = {}
        for w in new_words:
            counts[w] = counts.get(w, 0) + 1
        return {
            "most_common": max(counts, key=counts.get),
            "counts": counts,
            "unique_words": set(new_words),
        }

    def __str__(self):
        return f"DataAnalyzer: {len(self.numbers)} чисел, {len(self.words)} слов"


class ReportAnalyzer(DataAnalyzer):
    """Расширяет DataAnalyzer текстовым отчётом."""

    def text_report(self):
        """Собирает краткий отчёт из унаследованных методов."""
        nums = self.number_stats()
        words = self.word_stats()
        if nums is None or words is None:
            return "Недостаточно данных"
        return f"Среднее: {nums['avg']:.2f}, самое частое слово: {words['most_common']}"

import java.io.File

class DayOne {

    fun getMaxCalories(file: File): Long {

        return file.readText()
            .split("\r\n\r\n")
            .maxOf { sumStringLinesToLong(it) }
    }

    fun getNMaxCalories(file: File, n: Int): Long {

        return file.readText()
            .split("\r\n\r\n")
            .map { sumStringLinesToLong(it) }
            .sortedDescending()
            .take(n)
            .sum()
    }

    private fun sumStringLinesToLong(it: String) =
        it.split("\r\n")
            .sumOf { it.toLong() }
}
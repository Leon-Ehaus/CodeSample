import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertThrows
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import java.io.File

class DayOneTest {
    var underTest: DayOne = DayOne()
    var file: File = File("")

    @BeforeEach
    fun beforeEach() {
        file = File("./src/testInput/dayOneMaxCaloriesTest.txt")
        file.createNewFile()
        file.writeText(
            "1000\r\n" +
                    "2000\r\n" +
                    "3000\r\n" +
                    "\r\n" +
                    "3000\r\n" +
                    "\r\n" +
                    "5000\r\n" +
                    "6000\r\n" +
                    "\r\n" +
                    "7000\r\n" +
                    "8000\r\n" +
                    "9000\r\n" +
                    "\r\n" +
                    "10000"
        )
    }

    @Test
    fun getMaxCalories() {
        val maxCalories: Long = underTest.getMaxCalories(file)
        assertEquals(maxCalories, 24000)
    }

    @Test
    fun getNMaxCalories() {
        val maxCalories: Long = underTest.getNMaxCalories(file, 3)
        assertEquals(maxCalories, 45000)
    }

    @Test
    fun testGetMaxCaloriesWithEmptyFile() {
        val emptyFile = File("./src/testInput/dayOneMaxCaloriesTestEmpty.txt")
        emptyFile.createNewFile()
        assertThrows(NumberFormatException::class.java) { underTest.getMaxCalories(emptyFile) }
    }
}
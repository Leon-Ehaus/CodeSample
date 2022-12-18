import java.io.File

fun main() {
    val dayOne = DayOne()

    val maxCalDayOnePartOne: Long = dayOne.getNMaxCalories(File("./src/input/DayOne.txt"), 3)
    println(maxCalDayOnePartOne)
}
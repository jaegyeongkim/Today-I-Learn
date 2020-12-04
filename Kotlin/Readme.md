# Kotlin

[TOC]

## 문법

### Main

```kotlin
fun main() {
    '''
    이곳에 작성하면 된다.
    '''
}
```

### 함수

```kotlin
fun helloWorld() : Unit {	// return 이 없으면 Unit 생략 가능
    println("Hellow World") // 한 줄 출력
}

fun add(a : Int, b : Int) : Int {	// 변수 다음에 형식 나옴, 첫 단어 대문자
    								// 형식 생략되면 안 된다.
    return a+b
}
```

### val vs var

val = value (바뀌지 않는 것)

var = variable (바뀌는 것)

```kotlin
fun hi() {
    val a : Int = 10    // 변하지 않는 값
    var b : Int = 9     // 변하는 값
    // a = 100 => 오류가 발생
    b = 100

    val c = 100 // == val c : Int = 100
    var d = 100 // == var c : Int = 100

    var name = "Jake" // == var name : String = "Jake"
}
```

### String Template

${} 를 사용해서 표시

Python f-string 과 비슷

```kotlin
fun helloWorld() {
    val name = "Jake"
    val lastName = "Kim"
    println("my name is ${name + lastName} I'm 25")
    println("Is this 2\$?")	// $를 문자로 표현하고 싶을때는 \ 사용
    
    /*
    주석 표시
    */
}
```

### 조건문

```kotlin
fun maxBy(a : Int, b : Int) : Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}

fun maxBy2(a : Int, b : Int) = if(a>b) a else b	// 삼항 연산자와 비슷

fun checkNum(score : Int) {
    when(score) {                       // 다른 언어의 switch와 비슷한 역할
        0 -> println("this is 0")
        1 -> println("this is 1")
        2, 3 -> println("this is 2 or 3")
    }
    var b = when(score) {   // Expression 형식이면 else가 꼭 필요
        1 -> 1
        2 -> 2
        else -> 3
    }

    println("b : ${b}")
    when(score) {
        in 90..100 -> println("You are genius")	// 90 ~ 100 사이이면
        in 10..80 -> println("Good")
        else -> println("okay")
    }
}
```

### Expression vs Statement

Kotlin에서 모든 함수는 Expression이다.

|      | Expression     | Statement                           |
| ---- | -------------- | ----------------------------------- |
|      | 값을 반환한다. | 값을 내지 않아도 된다. 명령 하는 거 |

### Array and List

Array 처음 정해지는 사이즈가 있음

List 1. List (수정 불가능, 읽기 전용) 2. MutableList (수정 가능, 읽기, 쓰기 둘 다 가능)

```kotlin
fun array() {
    val array = arrayOf(1, 2, 3)
    val list = listOf(1, 2, 3)

    val array2 = arrayOf(1, "d", 3.4f)  // int, string, float
    val list2 = listOf(1, "d", 11L)

    array[0] = 3
    var result = list.get(0)

    val arrayList = arrayListOf<Int>()
    arrayList.add(10)
    arrayList.add(20)
    arrayList[0] = 20
}
```

### 반복문

```kotlin
fun forAndWhile() {
    val students = arrayListOf("Jake", "James", "Jenny", "Jennifer")

    for (name in students) {
        println("${name}")
    }
	// 인덱스와 함께 출력
    for ((index, name) in students.withIndex()) {
        println("${index+1}번째 학생 : ${name}")
    }

    var sum = 0
    for ( i in 1..10) {
        sum += i
    }
    println(sum)

    var sum2 = 0
    for ( i in 1..10 step 2) {
        sum2 += i
    }
    println(sum2)

    var sum3 = 0
    for ( i in 10 downTo 1) {
        sum3 += i
    }
    println(sum3)

    var sum4 = 0
    for ( i in 1 until 10) { // == 1..9
        sum4 += i
    }
    println(sum4)

    var index = 0
    while (index < 10) {
        println("current Index : ${index}")
        index++
    }
}
```

### Nullable / NonNull

```kotlin
fun nullcheck() {
    var name = "jake"
    var nullName : String? = null

    var nameInUpperCase = name.toUpperCase()
    var nullNameInUpperCase = nullName?.toUpperCase()   
    // ?의 의미: null이면 전체를 null로 반환
    // 아니면 toUpperCase를 반환
    // Null type인지를 아닌지를 확인하기 위해 사용
    
    // ?: 엘비스 연산자
	// val lastName : String? = null
    val lastName : String? = "Kim"
    val fullName = name + " " + (lastName?: "No LastName")  
    // lastName이 있으면 출력하고 없으면 뒤에 거를 출력
    println(fullName)
}
// !! 절대로 아니야!!
fun ignoreNulls(str : String?) {
    val mNotNull : String = str!!   // 변수 str이 절대로 Null 형식이 아니야!
    val upper = mNotNull.toUpperCase()

    val email : String?= "jake@naver.com"
    email?.let{                         // let: 앞에 있는 변수를 lambda식 내부로 넣어주는
                                        // Null 이 아니면 안에 식 실행
        println("my email is ${email}")
    }
}
```

### Class

```kotlin
class Human (val name : String = "Anonymous") { // 주 생성자

    constructor(name:String, age:Int) : this(name){ // 부 생성자
        println("my name is ${name}, ${age}years old")
    }
    init {  // 주 생성자
        println("New human has been born!!")
    }

    fun eatingCake() {
        println("This is so Yummy~")
    }

    fun singASong(){
        println("lalala")
    }
}

fun main() {
    val human = Human("minsu")
    val stranger = Human()
    human.eatingCake()
    println("this human's name is ${stranger.name}")
    val mom = Human( "Kuri", 52)
}
```

상속

```kotlin
open class Human (val name : String = "Anonymous") { // 주 생성자

    constructor(name:String, age:Int) : this(name){ // 부 생성자
        println("my name is ${name}, ${age}years old")
    }
    init {  // 주 생성자
        println("New human has been born!!")
    }

    fun eatingCake() {
        println("This is so Yummy~")
    }

    open fun singASong(){
        println("lalala")
    }
}

class Korean : Human() {				// 상속 (부모가 open을 해줘야 뱓을 수 있음)
    override fun singASong(){			// 상속의 관계에 있는 클래스 간에 하위 클래스가
        								// 상위 클래스와 '완전 동일한 메소드'를 덮어쓴다.
        super.singASong()				// 상속
        println("라라라")
        println("my name is ${name}")	// Human에 있는 name을 가져옴
    }
}

fun main() {
    val korean = Korean()
    korean.singASong()
}
```

### Lambda

#### Lambda의 기본

람다식은 우리가 마치 value 처럼 다룰 수 있는 익명함수이다.

1. 메소드의 파라미터로 넘겨줄 수 있다. fun maxBy(a : Int)
2. return 값으로 사용할 수 없다.
3. 타입 추론이 가능하다. 단, 기본적인 부분은 적어줘야한다.

```kotlin


// 람다의 기본정의
// val lamdaName : Type = (argumentList -> codeBody)

val square : (Int) -> (Int) = {number -> number+number}

val nameAge = {name : String, age : Int ->
    "my name is ${name} I'm ${age}"
}

fun main() {
    println(square(12))
    println(nameAge("jake", 26))
}
```

#### 확장 함수

```kotlin
fun main() {
    val a = "Jake Said "
    val b = "Mac Said "
    println(a.pizzaIsGreat())
    println(b.pizzaIsGreat())

    println(extendString("ariana", 27))
}

// 확장함수
val pizzaIsGreat : String.() -> String = {
    this + "Pizza is the best!"
}

fun extendString(name : String, age : Int) : String {
    val introduceMyself : String.(Int) -> String = {"I am ${this} and ${it} years old"} 
    // this: Object를 가리키고, it: 파타미터가 하나일 경우
    return name.introduceMyself(age)
}
```

#### 람다의 리턴

```kotlin
fun main() {
    println(calculateGrade(98))
    println(calculateGrade(981))
}
// 람다의 Return
val calculateGrade : (Int) -> String = {
    when(it) {
        in 0..40 -> "Fail"
        in 41..70 -> "Pass"
        in 71..100 -> "Perfect"
        else -> "Error"
    }
}
```

#### 람다를 표현하는 2가지 방법

```kotlin
fun main() {
    val lambda = {number : Double ->
        number == 4.3213
    }
    println(invokeLambda(lambda))
    println(invokeLambda({it > 3.22}))
    println(invokeLambda { it > 3.22 })
}

fun invokeLambda(lambda : (Double) ->  Boolean) : Boolean {
    return lambda(5.2343)
}
```

##### 익명함수

1. Kotlin interface가 아닌 자바 인터페이스여야 한다.
2. 그 인터페이스에 딱 하나의 함수만 있어야한다.

### Data Class

관리하기 편하다.

```kotlin
data class Ticket(val companyName : String, val name : String, var data : String, var seatNumber : Int)

fun main() {
    val ticketA = Ticket("koreanAir", "Jake", "2020-12-04", 14)

}
```

Class와 비교하면

```kotlin
data class Ticket(val companyName : String, val name : String, var data : String, var seatNumber : Int)
// data class
class TicketNormal(val companyName : String, val name : String, var data : String, var seatNumber : Int)
// class
fun main() {
    val ticketA = Ticket("koreanAir", "Jake", "2020-12-04", 14)
    val ticketB = TicketNormal("koreanAir", "Jake", "2020-12-04", 14)
    println(ticketA)	// 
    println(ticketB)	// 주소값으로 나옴
}
>> Ticket(companyName=koreanAir, name=Jake, data=2020-12-04, seatNumber=14)
>> com.example.myapplication.TicketNormal@5cad8086
```

### Companion object

Companion object의 역할: Private Method or Property 읽을 수 있음, Java의 Static 역할

```kotlin
class Book private constructor(val id : Int, val name : String) {

    companion object BookFactory : IdProvider{

        override fun getId(): Int{
            return 444
        }
        val myBook = "new book"
        fun create() = Book(0, "animal fare")
        fun create1() = Book(0, myBook)
        fun create2() = Book(getId(), myBook)
    }
}

interface IdProvider {
    fun getId() : Int
}

fun main() {
    val book = Book.create()
    val book1 = Book.create1()
    val book2 = Book.create2()
    println("${book.id} ${book.name}")
    println("${book1.id} ${book1.name}")
    println("${book2.id} ${book2.name}")
}
```

### Object

Singleton Pattern
이 모든 앱을 실행할때 딱 한번 실행된다.  -> 불필요한 메모리 사용 X

```kotlin
object CarFactory {
    val cars = mutableListOf<Car>()

    fun makeCar(horsePower: Int) : Car {
        val car = Car(horsePower)
        cars.add(car)
        return car
    }
}

data class Car(val horsePower : Int)

fun main() {
    val car = CarFactory.makeCar(10)
    val car2 = CarFactory.makeCar(200)
    
    println(car)
    println(car2)
    println(CarFactory.cars.size.toString())
}
>> Car(horsePower=10)
>> Car(horsePower=200)
>> 2
```


public class IntermediateRecap {

    public static void main(String[] args) {

        Student student = new Student("miraz", 24);
        System.out.println(student.getDetails());

    }

}

class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getDetails() {
        return "student: " + name + " age: " + age;
    }
}

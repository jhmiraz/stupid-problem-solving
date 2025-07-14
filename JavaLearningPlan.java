class JavaLearningPlan {

    public static void main(String[] args) {
        int age = 25;
        char b = 'a';
        String name = "Miraz";
        double salary = 5000.00;
        boolean isStudent = true;

        System.out.println("name: " + name + "age: " + age + "salary: " + salary + b + " " + isStudent);

        if (age >= 18) {
            System.out.println(name + " is adult");
        } else {
            System.out.println(name + " is not an adult");
        }

        for (int i = 1; i <= 5; i++) {
            System.out.println("count: " + i);
        }

        int num = 5;
        System.out.println("squire of " + num + " is " + claculateSquire(num));
    }

    static int claculateSquire(int num) {
        return num * num;

    }

}

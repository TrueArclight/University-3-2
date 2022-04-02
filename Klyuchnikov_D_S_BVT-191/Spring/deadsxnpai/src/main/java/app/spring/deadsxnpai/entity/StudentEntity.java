package app.spring.deadsxnpai.entity;


import javax.persistence.*;

@Entity
@Table(name = "students")
public class StudentEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long Id;

    @Column(nullable = false, length = 100)
    private String firstName;

    @Column(nullable = false, length = 100)
    private String secondName;

    @Column(nullable = false, length = 100)
    private String thirdName;

    @Column(nullable = false, length = 100)
    private String year;

    @Column(nullable = false, length = 100)
    private String gender;

    @ManyToOne
    @JoinColumn(name = "class_id")
    private ClassEntity student;


    public StudentEntity(){}

    public long getId() {
        return Id;
    }

    public void setId(long id) {
        Id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getSecondName() {
        return secondName;
    }

    public void setSecondName(String secondName) {
        this.secondName = secondName;
    }

    public String getThirdName() {
        return thirdName;
    }

    public void setThirdName(String thirdName) {
        this.thirdName = thirdName;
    }

    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public ClassEntity getStudent() {
        return student;
    }

    public void setStudent(ClassEntity student) {
        this.student = student;
    }
}

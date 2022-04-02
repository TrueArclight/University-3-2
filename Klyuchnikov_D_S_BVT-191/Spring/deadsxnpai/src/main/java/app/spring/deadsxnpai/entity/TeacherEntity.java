package app.spring.deadsxnpai.entity;

import javax.persistence.*;

@Entity
@Table(name = "teachers")
public class TeacherEntity {
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

    @Column(nullable = false, length = 100)
    private String subject;

    @OneToOne
    @JoinColumn(name = "class_id")
    private ClassEntity teacher;
    public TeacherEntity(){}

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

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public ClassEntity getTeacher() {
        return teacher;
    }

    public void setTeacher(ClassEntity teacher) {
        this.teacher = teacher;
    }
}

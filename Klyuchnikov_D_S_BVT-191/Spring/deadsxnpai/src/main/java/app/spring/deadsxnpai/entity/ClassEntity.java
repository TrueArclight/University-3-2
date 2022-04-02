package app.spring.deadsxnpai.entity;

import javax.persistence.*;
import java.util.List;

@Entity
@Table(name = "class")
public class ClassEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    @Column(nullable = false, length = 100)
    private String code;
    @Column(nullable = false, length = 100)
    private String year;

    @OneToMany(cascade = CascadeType.ALL, mappedBy = "student")
    private List<StudentEntity> studentEntityList;

    @OneToOne(cascade = CascadeType.ALL, mappedBy = "teacher")
    private TeacherEntity teacher_id;

    public List<StudentEntity> getPupilsEntityList() {
        return studentEntityList;
    }

    public void setPupilsEntityList(List<StudentEntity> studentEntityList) {
        this.studentEntityList = studentEntityList;
    }
    public ClassEntity() {
    }

    public TeacherEntity getTeacher_id() {
        return teacher_id;
    }

    public void setTeacher_id(TeacherEntity teacher_id) {
        this.teacher_id = teacher_id;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

}

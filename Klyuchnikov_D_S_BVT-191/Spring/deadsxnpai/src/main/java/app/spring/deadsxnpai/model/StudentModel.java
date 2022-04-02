package app.spring.deadsxnpai.model;

import app.spring.deadsxnpai.entity.StudentEntity;

public class StudentModel {
    Long id;
    String fistName;
    String secondName;
    String gender;
    public static StudentModel toModel(StudentEntity student){
        StudentModel model = new StudentModel();
        model.setId(student.getId());
        model.setFistName(student.getFirstName());
        model.setSecondName(student.getSecondName());
        model.setGender(student.getGender());
        return model;
    }
    public StudentModel(){

    }
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getFistName() {
        return fistName;
    }

    public void setFistName(String fistName) {
        this.fistName = fistName;
    }

    public String getSecondName() {
        return secondName;
    }

    public void setSecondName(String secondName) {
        this.secondName = secondName;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
}

package app.spring.deadsxnpai.model;

import app.spring.deadsxnpai.entity.TeacherEntity;

public class TeacherModel {
    Long id;
    String fistName;
    String secondName;
    String gender;
    String subject;
    public static TeacherModel toModel(TeacherEntity teacher){
        TeacherModel model = new TeacherModel();
        model.setId(teacher.getId());
        model.setFistName(teacher.getFirstName());
        model.setSecondName(teacher.getSecondName());
        model.setGender(teacher.getGender());
        model.setSubject(teacher.getSubject());
        return model;
    }
    public TeacherModel(){}

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

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
}

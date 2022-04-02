package app.spring.deadsxnpai.model;

import app.spring.deadsxnpai.entity.ClassEntity;


public class ClassModel {
    Long id;
    String code;
    String year;

    public static ClassModel toModel(ClassEntity entity){
        ClassModel model = new ClassModel();
        model.setId(entity.getId());
        model.setCode(entity.getCode());
        model.setYear(entity.getYear());
        return model;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
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

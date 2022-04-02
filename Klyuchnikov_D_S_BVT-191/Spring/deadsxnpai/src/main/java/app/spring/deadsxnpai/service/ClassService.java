package app.spring.deadsxnpai.service;

import app.spring.deadsxnpai.entity.ClassEntity;

import app.spring.deadsxnpai.exceptions.CodeAlreadyExist;
import app.spring.deadsxnpai.exceptions.CodeNotFoundException;
import app.spring.deadsxnpai.model.ClassModel;
import app.spring.deadsxnpai.repository.ClassRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ClassService {
    @Autowired
    private ClassRepository classRepository;

    public ClassEntity createClass(ClassEntity classEntity) throws CodeAlreadyExist {
        if(classRepository.findByCode(classEntity.getCode()) != null){
             throw new CodeAlreadyExist("Уже существует такой класс");
        }
        return classRepository.save(classEntity);
    }

    public long deleteClass(long id){
        classRepository.deleteById(id);
        return id;
    }
    public ClassModel getOne(long id) throws CodeNotFoundException {
        ClassEntity classEntity = classRepository.findById(id).get() ;
        if(classEntity == null){
            throw new CodeNotFoundException("Класс не найден");
        }
        return ClassModel.toModel(classEntity);
    }

}

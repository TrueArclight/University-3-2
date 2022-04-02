package app.spring.deadsxnpai.service;

import app.spring.deadsxnpai.entity.ClassEntity;
import app.spring.deadsxnpai.entity.TeacherEntity;
import app.spring.deadsxnpai.exceptions.TeacherNotFoundException;
import app.spring.deadsxnpai.model.TeacherModel;
import app.spring.deadsxnpai.repository.ClassRepository;
import app.spring.deadsxnpai.repository.TeacherRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class TeacherService {
    @Autowired
    private TeacherRepository teacherRepository;
    @Autowired
    private ClassRepository classRepository;

    public TeacherEntity createTeacher(TeacherEntity teacher, Long classId){
        ClassEntity classEntity = classRepository.findById(classId).get();
        teacher.setTeacher(classEntity);
        return teacherRepository.save(teacher);
    }

    public long deleteTeacher(long id){
        teacherRepository.deleteById(id);
        return id;
    }

    public TeacherModel getOne(long id) throws TeacherNotFoundException {
        TeacherEntity teacher = teacherRepository.findById(id).get() ;
        if(teacher == null){
            throw new TeacherNotFoundException("Ученик не найден");
        }
        return TeacherModel.toModel(teacher);
    }
}

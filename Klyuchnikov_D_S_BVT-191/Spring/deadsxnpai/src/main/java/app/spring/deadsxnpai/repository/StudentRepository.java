package app.spring.deadsxnpai.repository;

import app.spring.deadsxnpai.entity.StudentEntity;
import org.springframework.data.repository.CrudRepository;

public interface StudentRepository extends CrudRepository<StudentEntity, Long> {
}

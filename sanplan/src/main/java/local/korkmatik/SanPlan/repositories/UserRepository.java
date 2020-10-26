package local.korkmatik.SanPlan.repositories;

import local.korkmatik.SanPlan.models.user.User;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends MongoRepository<User, Integer> {

}

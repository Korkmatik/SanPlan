package local.korkmatik.SanPlan.repositories.user;

import local.korkmatik.SanPlan.models.user.Role;
import local.korkmatik.SanPlan.models.user.User;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface UserRepository extends MongoRepository<User, Integer> {

    User findByEmail(String email);
    List<User> findByRolesContains(Role role);
}

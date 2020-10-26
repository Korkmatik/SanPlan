package local.korkmatik.SanPlan.repositories.user;

import local.korkmatik.SanPlan.models.user.Role;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RoleRepository extends MongoRepository<Role, String> {

    Role findByRole(String role);
}

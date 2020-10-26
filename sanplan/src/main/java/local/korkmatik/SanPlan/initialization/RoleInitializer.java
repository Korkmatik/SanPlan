package local.korkmatik.SanPlan.initialization;

import local.korkmatik.SanPlan.models.user.Role;
import local.korkmatik.SanPlan.repositories.user.RoleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class RoleInitializer {

    @Autowired
    private RoleRepository roleRepository;

    public Role createAdminRoleIfNotExists() {
        return createRoleIfNotExists(Role.Roles.ADMIN);
    }

    public Role createUserRoleIfNotExists() {
        return createRoleIfNotExists(Role.Roles.USER);
    }

    private Role createRoleIfNotExists(Role.Roles role) {
        String roleStr = role.name();

        Role dbRole = roleRepository.findByRole(roleStr);
        if (dbRole == null) {
            Role newRole = new Role();
            newRole.setRole(roleStr);
            roleRepository.save(newRole);
        }

        return dbRole;
    }
}

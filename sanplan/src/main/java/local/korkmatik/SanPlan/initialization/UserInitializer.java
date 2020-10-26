package local.korkmatik.SanPlan.initialization;

import local.korkmatik.SanPlan.models.user.Role;
import local.korkmatik.SanPlan.models.user.User;
import local.korkmatik.SanPlan.repositories.user.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import javax.swing.text.html.Option;
import java.util.List;
import java.util.Optional;
import java.util.Set;

@Component
public class UserInitializer {

    @Autowired
    private PasswordEncoder passwordEncoder;
    @Autowired
    private UserRepository userRepository;

    public Optional<User> createDummyAdminUser(Role role) {
        List<User> adminUsers = userRepository.findByRolesContains(role);
        User adminUser = null;

        if (adminUsers.isEmpty()) {
            adminUser = new User();
            adminUser.setFirstName("Admin");
            adminUser.setLastName("Admin");
            adminUser.setRoles(Set.of(role));
            adminUser.setEmail("admin@localhost");
            adminUser.setEnabled(true);
            adminUser.setPassword(passwordEncoder.encode("admin"));
            userRepository.save(adminUser);
        }

        return Optional.ofNullable(adminUser);
    }
}

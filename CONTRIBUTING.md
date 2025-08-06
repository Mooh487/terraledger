# 🤝 Contributing to TerraLedger Carbon Exchange

Thank you for your interest in contributing to TerraLedger! We're building the future of transparent carbon markets, and every contribution helps create a more sustainable world.

## 🌍 Our Mission

TerraLedger aims to eliminate greenwashing in carbon markets through AI-verified, blockchain-native solutions. We believe in:
- **Transparency**: Every carbon credit should be verifiable
- **Accessibility**: Climate action should be available to everyone
- **Innovation**: Leveraging cutting-edge technology for environmental good
- **Community**: Building together for a sustainable future

## 🚀 Getting Started

### Prerequisites
- **Node.js** 18+ and npm
- **Python** 3.9+ and pip
- **Git** for version control
- **Hedera Testnet Account** (for blockchain features)

### Development Setup
1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/terraledger-carbon-exchange.git
   cd terraledger-carbon-exchange
   ```
3. **Install dependencies**:
   ```bash
   npm run setup
   ```
4. **Configure environment**:
   ```bash
   cp backend/.env.example backend/.env
   # Edit backend/.env with your credentials
   ```
5. **Start development servers**:
   ```bash
   npm run dev
   ```

## 🛠️ Development Workflow

### Branch Strategy
- **main**: Production-ready code
- **develop**: Integration branch for features
- **feature/**: New features (`feature/carbon-nft-updates`)
- **fix/**: Bug fixes (`fix/validation-error`)
- **docs/**: Documentation updates (`docs/api-reference`)

### Making Changes
1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-amazing-feature
   ```
2. **Make your changes** following our coding standards
3. **Test your changes**:
   ```bash
   npm run test
   npm run lint
   ```
4. **Commit with conventional commits**:
   ```bash
   git commit -m "feat: add satellite imagery validation"
   ```
5. **Push and create a Pull Request**

### Commit Message Convention
We use [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

## 📋 Areas for Contribution

### 🌲 AI & Machine Learning
- Improve forest verification algorithms
- Enhance satellite imagery analysis
- Develop predictive carbon sequestration models
- Create anomaly detection systems

**Skills needed**: Python, TensorFlow, Computer Vision, Remote Sensing

### 🔗 Blockchain Development
- Enhance Hedera integrations
- Implement new HCS-10 features
- Optimize smart contracts
- Develop cross-chain bridges

**Skills needed**: Solidity, Hedera SDK, Blockchain protocols

### 🎨 Frontend Development
- Build beautiful, accessible interfaces
- Improve user experience
- Add data visualizations
- Implement mobile responsiveness

**Skills needed**: React, TypeScript, Tailwind CSS, UX/UI Design

### 📊 Data & Analytics
- Develop impact measurement tools
- Create reporting dashboards
- Build data pipelines
- Implement real-time monitoring

**Skills needed**: Data Science, Analytics, Visualization

### 📚 Documentation
- Improve API documentation
- Create tutorials and guides
- Write technical blog posts
- Translate content

**Skills needed**: Technical Writing, API Documentation

### 🧪 Testing & Quality Assurance
- Expand test coverage
- Implement integration tests
- Performance testing
- Security auditing

**Skills needed**: Testing Frameworks, Security, Performance

## 📝 Coding Standards

### Python (Backend)
- Follow **PEP 8** style guide
- Use **type hints** for all functions
- Write **docstrings** for modules, classes, and functions
- Maintain **>80% test coverage**

```python
def verify_forest(lat: float, lon: float) -> Dict[str, Any]:
    """
    Verify forest coverage at a specific location.
    
    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        
    Returns:
        Dict containing verification results
    """
    # Implementation here
```

### TypeScript (Frontend)
- Use **ESLint** and **Prettier** configurations
- Follow **React best practices**
- Use **TypeScript strict mode**
- Write **component documentation**

```typescript
interface CarbonCreditProps {
  /** Unique identifier for the carbon credit */
  creditId: string;
  /** Current verification status */
  status: 'pending' | 'verified' | 'rejected';
  /** Callback when credit is selected */
  onSelect: (creditId: string) => void;
}

export const CarbonCredit: React.FC<CarbonCreditProps> = ({
  creditId,
  status,
  onSelect
}) => {
  // Component implementation
};
```

### General Guidelines
- **Write clear, self-documenting code**
- **Add comments for complex logic**
- **Keep functions small and focused**
- **Use meaningful variable names**
- **Handle errors gracefully**

## 🧪 Testing Guidelines

### Backend Testing
```bash
# Run all tests
cd backend && pytest

# Run with coverage
pytest --cov=terraledger

# Run specific test file
pytest terraledger/tests/test_ai_validator.py
```

### Frontend Testing
```bash
# Run tests
cd frontend && npm test

# Run with coverage
npm run test:coverage
```

### Test Requirements
- **Unit tests** for all new functions
- **Integration tests** for API endpoints
- **Component tests** for React components
- **E2E tests** for critical user flows

## 📖 Documentation Standards

### API Documentation
- Use **OpenAPI/Swagger** specifications
- Include **request/response examples**
- Document **error codes** and messages
- Provide **authentication details**

### Code Documentation
- **README files** for each module
- **Inline comments** for complex logic
- **Type definitions** and interfaces
- **Usage examples** for public APIs

## 🔍 Code Review Process

### Submitting Pull Requests
1. **Ensure all tests pass**
2. **Update documentation** if needed
3. **Add screenshots** for UI changes
4. **Reference related issues**
5. **Request review** from maintainers

### Review Criteria
- ✅ **Functionality**: Does it work as expected?
- ✅ **Code Quality**: Is it clean and maintainable?
- ✅ **Performance**: Does it impact system performance?
- ✅ **Security**: Are there any security concerns?
- ✅ **Documentation**: Is it properly documented?
- ✅ **Tests**: Are there adequate tests?

## 🌟 Recognition

We believe in recognizing our contributors:
- **Contributors** listed in README
- **Special mentions** in release notes
- **Contributor badges** for significant contributions
- **Early access** to new features

## 🆘 Getting Help

### Community Support
- 💬 **Discord**: [Join our community](https://discord.gg/terraledger)
- 📧 **Email**: dev@terraledger.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/terraledger/issues)

### Mentorship Program
New to open source? We offer mentorship for:
- First-time contributors
- Students and early-career developers
- Career changers into climate tech

## 📊 Contribution Metrics

We track and celebrate:
- **Code contributions** (commits, PRs)
- **Documentation improvements**
- **Bug reports and fixes**
- **Community engagement**
- **Educational content creation**

## 🎯 Contribution Ideas

### Good First Issues
- Fix typos in documentation
- Add unit tests for existing functions
- Improve error messages
- Add loading states to UI components

### Advanced Contributions
- Implement new AI models
- Add support for new blockchain networks
- Build mobile applications
- Create data visualization tools

## 🔒 Security

### Reporting Security Issues
- **DO NOT** open public issues for security vulnerabilities
- **Email** security@terraledger.com with details
- **Include** steps to reproduce
- **Expect** acknowledgment within 48 hours

### Security Best Practices
- Never commit API keys or secrets
- Use environment variables for configuration
- Validate all user inputs
- Follow OWASP guidelines

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

### Our Values
- **Respect**: Treat everyone with respect and kindness
- **Inclusion**: Welcome contributors from all backgrounds
- **Collaboration**: Work together towards common goals
- **Learning**: Support each other's growth and learning

## 🎉 Thank You!

Every contribution, no matter how small, makes a difference in our mission to create transparent carbon markets. Together, we're building a more sustainable future!

---

**Questions?** Don't hesitate to reach out. We're here to help you make your first contribution to climate tech! 🌍💚

# JetPunk Solver 🤖➡️📝

*From a hacky script to a modular tool - now with 90% less redundancy!*

Automate answers for [JetPunk](https://www.jetpunk.com) quizzes.
**Supports**: Fill-in-the-blank, Multiple Choice, and "All Words" quizzes.

---

## 🚀 Why This Exisits
```python
# Original Motivation (August 2024)
if bored_with_quizzes and curious_about_web_scrapping:
    build_jetpunk_solver()  # "For science!"
```

Started as a **quick hack** to explore web scraping, now refactored into a **maintainable tool** with:
- ✅ **Modular design** (ABC classes, clean separation of concerns)
- ✅ **Config-driven** (timeouts, delays in `config.ini`)
- ✅ **Auto-detection** of quiz types (no manual selection!)


## 📦 Installation
```bash
git clone https://github.com/youssef3698/jetpunk-solver.git
cd jetpunk-solver
pip install -e .
```

## 🎯 Features
|Feature|Old Code (v0.1)|New Code(v1.0)|
|:----------|:----------:|:----------:|
|**Quiz Detection**|Manual script selection|Auto-detection|
|**Code Duplication**|80+ lines per quiz type|~10 lines per quiz type|
|**Configurability**|Hardcoded values|`config.ini` support|

## 🔧 Usage
### Basic (Print Answers)
```bash
jetpunk-solver <quiz_url>
```
### Automation (Type Answers)
```bash
jetpunk-solver <quiz_url> --auto
```

*Configure delays in `src/config/config.ini`*

## 🛠️ Project Evolution
### Phase 1: The "Cheat Mode" Prototype
- **Pain Points**
  - Copy-pasted code for each quiz type
  - No timeout handling (failed requests hung forever)
  - Only usable via command-line prompts

### Phase 2: The Great Refactoring
- **Solutions**
  - **ABC Classes**: Shared logic in `BaseQuizType`
  - **Centralized Config**: Timeouts, delays in `config.ini`
  - **Polymorphism**: Auto-detection with `infer_quiz_type()`

## 📂 Project Structure
```bash
src/
|-- solver/
|   |-- quiz_types/   # ABC-based handlers
|   |-- utils/        # Shared helpers (e.g., clean_answer_text)
|   |-- config/       # config.ini loader
```

## 🌟 Future Plans
1. **Tests**: Proper test coverage is not yet implemented (help wanted!)
2. **More Quiz Types**: Image-based quizzes, map quizzes, etc. (not sure if handled by current tests)
3. **Better Detection**: Edge cases for quiz auto-detection

## 🤝 How to Contribute
You're welcome to:
1. **Report Bugs**
  - Found a quiz that doesn't work? Share the URL and error in Issues
2. **Suggest Improvements**
  - Ideas for new features or UX tweaks? I'd love to hear them!
3. **Add Tests**
  - Want to help implement pytest? This is the current top priority!


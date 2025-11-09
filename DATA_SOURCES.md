# Data Sources Documentation

## Faculty Data

### Primary Source (ACTIVE)
**File**: `faculty_data.json`
- **Location**: Root directory
- **Size**: 15KB
- **Structure**: Categorized by faculty type (fulltime, parttime, practical, honorary, joint)
- **Used by**: All faculty pages via JavaScript dynamic loading
- **Format**:
  ```json
  {
    "fulltime": [...],
    "parttime": [...],
    "practical": [...],
    "honorary": [...],
    "joint": [...]
  }
  ```

### Photo Mapping (REFERENCE)
**File**: `faculty-mapping.csv`
- **Location**: Root directory
- **Purpose**: Reference for photo filename to faculty member mapping
- **Format**: CSV with columns: ID, Name, Photo filename

### Legacy/Deprecated Sources (DO NOT USE)
- ❌ `data/teachers.json` - Old format, not used by any page
- ❌ `archive/practical_faculty_data.json` - Archived old data

## News and Activities Data

### Primary Source (ACTIVE)
**File**: `data/content.csv`
- **Format**: CSV with columns: title, date, category, time, location, content
- **Categories**: news, activity
- **Used by**: Should be used by homepage.js (currently using mock data - needs fix)

### Individual HTML Files (LEGACY)
- `news/*.html` - 22 individual news article files
- `activities/*.html` - 97 individual activity files
- **Status**: Legacy files, consider migration to dynamic loading

## Single Source of Truth Rule

⚠️ **IMPORTANT**: Always use `faculty_data.json` as the single source of truth for faculty information.

When updating faculty data:
1. Edit `faculty_data.json`
2. Update `faculty-mapping.csv` if adding/changing photos
3. Ensure photo files exist in `images/faculty/`
4. Run `python3 build-templates.py` if templates changed

## Data Validation

Before committing data changes, verify:
- [ ] JSON is valid (use `python3 -m json.tool faculty_data.json`)
- [ ] All photo paths exist
- [ ] No duplicate IDs
- [ ] Required fields present (id, name, photo)

---

*Last updated: 2025-11-08*

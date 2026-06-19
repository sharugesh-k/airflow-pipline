# Architecture Diagram Downloads

## Warehouse ETL Pipeline - Architecture Visualization

This folder contains the architecture diagrams for the Warehouse ETL Pipeline project.

### Files Available:

1. **architecture-diagram.svg** - Scalable Vector Graphics (Best for Web & Presentations)
   - High quality, scales to any size
   - Perfect for LinkedIn, portfolios, and presentations
   - Editable in design tools

### Download Instructions:

#### Option 1: Direct Download from GitHub
1. Go to: https://github.com/sharugesh-k/airflow-pipline
2. Click on `docs/architecture-diagram.svg`
3. Click the "Download" button (or Raw)
4. Save to your local PC

#### Option 2: Using Git CLI
```bash
git clone https://github.com/sharugesh-k/airflow-pipline.git
cd airflow-pipline/docs
# Your files are ready in this directory
```

#### Option 3: Using Raw GitHub URL
Right-click and "Save As":
```
https://raw.githubusercontent.com/sharugesh-k/airflow-pipline/main/docs/architecture-diagram.svg
```

### Using the Diagram:

- **LinkedIn Posts**: Upload directly to LinkedIn - it will render perfectly
- **Presentations**: Use in PowerPoint, Google Slides, or Keynote
- **Documentation**: Embed in README.md or technical docs
- **Web**: Add to portfolio website

### What's Included in the Diagram:

```
Data Flow:
API → Extract → Transform → Load → PostgreSQL

Orchestration:
├── DAG (Task 1, 2, 3)
├── Scheduler (Daily @daily)
└── Executor & Monitoring

Infrastructure:
├── PostgreSQL Data Warehouse
├── Virtual Environments (Isolated)
└── GitHub Version Control
```

### Format Details:

**SVG (Scalable Vector Graphics)**
- Best for: Web, presentations, scalability
- Can be edited in: Adobe Illustrator, Figma, Inkscape, online SVG editors
- File size: Lightweight
- Quality: Always crisp at any size

---

**Last Updated:** June 19, 2026
**Project:** Warehouse ETL Pipeline with Apache Airflow
**GitHub:** https://github.com/sharugesh-k/airflow-pipline

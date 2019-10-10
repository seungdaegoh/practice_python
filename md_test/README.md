## Log Analyzer Tool

### Overview
```mermaid
graph LR
I[IN: log files] --> A[Log Analyzer]

A --> O[OUT: html print]
```
### pre processing
```mermaid
graph LR
I[IN: log files] --> A[Log Analyzer]
A--> C{what kind of file?}
C -->|main| D[run - proc_main]
C -->|radio| D
C -->|kernel| E[run - proc_kernel]
C -->|memory| F[run - proc_memory]
C -->|pcap| G[run - proc_pcap]
```

### processing of parsing
```mermaid
graph LR
A[IN: logfiles] -->B(proc_***)
C[IN: key_words.csv] -->B(proc_***)

B --> F[OUT: timeline_top*.csv]
B --> G[OUT: timeline_proc*.csv]

	```
### processing of html output
```mermaid
graph LR

J[IN: timeline_**.csv] --> H(make_html)
H --> O[OUT: result.html]
```


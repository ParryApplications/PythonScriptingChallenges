from pathlib import Path;
import logging;

logFilePath = Path("server.log");
mainPyLogs = Path("mainPyLogs.log");

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(mainPyLogs,mode='w',encoding="utf-8")
    ]
);

errorCount = 0;
errorMessages = set();

with open(logFilePath,mode="r", encoding="utf-8") as file:
    for n in file:
        try:
            logging.info("Reading a line...");
            # print(type(n));
            if "ERROR" in n:
                errorCount += 1;
                errorMessages.add(n);
        except:
            logging.error("Line Read unsuccess, Uncompleted.");
        else:
            logging.info("Line Read Successfully Completed.");
        finally:
            logging.info("Moving to next line...");


outputFilePath = Path("error_report.txt");
errorMessages = list(errorMessages);

with open(outputFilePath, mode='w',encoding="utf-8") as file:
    file.write("=== ERROR REPORT ===\n");
    file.write(f"Total Errors Found: {errorCount}\n");
    for index,errorMsg in enumerate(errorMessages, start=1):
        file.write(f"{index}. {errorMsg}")

logging.info("Complete File Analyzed");
print("Operation Completed.")
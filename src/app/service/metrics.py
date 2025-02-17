from app.common.utils import create_metric_report


class Service():
    def report(report_number):
        try:
            report = create_metric_report(report_number=report_number)
            return {
                "message": "Report generated successfully.",
                "data": report,
            }
        except Exception as e:
            raise Exception(str(e))
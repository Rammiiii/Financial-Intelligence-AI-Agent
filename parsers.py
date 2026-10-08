from pydantic import BaseModel, Field
from typing import List, Optional

class FinancialMetric(BaseModel):
    metric_name: str = Field(description="اسم المؤشر أو البند المالي مثل Revenue, Net Income, CapEx")
    value: str = Field(description="القيمة المالية مع العملة والسنة")
    trend: Optional[str] = Field(description="الاتجاه مقارنة بالفترة السابقة إن وجد (زيادة/انخفاض)")

class FinancialAnalysisReport(BaseModel):
    company_name: str = Field(description="اسم الشركة")
    period: str = Field(description="الفترة المالية المذكورة (مثل FY 2024 أو Q3)")
    metrics: List[FinancialMetric] = Field(description="قائمة بالأرقام والمؤشرات المالية المستخرجة")
    key_risks: List[str] = Field(description="المخاطر الرئيسية المذكورة")
    summary: str = Field(description="ملخص تنفيذي لأداء الشركة")
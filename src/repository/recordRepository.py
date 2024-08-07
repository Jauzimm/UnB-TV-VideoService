from sqlalchemy.orm import Session

from domain import recordSchema
from model import recordModel
from fastapi import HTTPException 

def create_record(db: Session, record: recordSchema.RecordCreate):
   db_record = recordModel.Record(
       user_id=record.user_id.strip(),
       videos=record.videos
   )
   db.add(db_record)
   db.commit()
   db.refresh(db_record)
   print(f"Created record: user_id={db_record.user_id}")
   return db_record

def get_record(db: Session, record: recordSchema.RecordGet):
   user_id = record.user_id.strip()
   record_entry = db.query(recordModel.Record).filter(
       recordModel.Record.user_id == user_id
   ).first()
   print(f"Query Result: {record_entry}")
   if record_entry:
       print(f"Check Record Founds")
       return record_entry.videos
   print(f"Check Record Not Found")
   return False

"""资料与现有领域接口的核对。"""
import unittest,tempfile,json
from pathlib import Path
from lake.storage import Storage
from lake.merge import inspect

class DomainTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name);self.store=Storage(self.root/'objects')
        self.data=json.loads(Path('data/source.json').read_text(encoding='utf-8'))
    def test_existing_reader(self):
        self.assertTrue(inspect(self.data,self.store,self.root))

    def test_unique_final_rows(self):
        from lake.merge import unique_rows
        self.assertTrue(unique_rows(self.data['target'],['shipment']))
        with self.assertRaises(ValueError):unique_rows(self.data['target']+[dict(self.data['target'][0],row_id='other')],['shipment'])

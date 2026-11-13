import asyncio, importlib.util, sys, types
from pathlib import Path

root = Path(__file__).resolve().parent
if not (root / 'hub.py').exists():
    root = root.parent / 'custom_components' / 'aohai_fsc_g3'
package = types.ModuleType('fake'); package.__path__ = [str(root)]
sys.modules['fake'] = package
ha = types.ModuleType('homeassistant'); exc = types.ModuleType('homeassistant.exceptions')
exc.ConfigEntryNotReady = type('ConfigEntryNotReady', (Exception,), {})
sys.modules['homeassistant'] = ha; sys.modules['homeassistant.exceptions'] = exc
pm = types.ModuleType('pymodbus'); client = types.ModuleType('pymodbus.client'); errors = types.ModuleType('pymodbus.exceptions')
errors.ModbusException = type('ModbusException', (Exception,), {})
class Response:
    registers = [2300]
    def isError(self): return False
class FakeClient:
    def __init__(self, **kw): self.kw = kw; self.connected = False; self.calls = []
    async def connect(self): self.connected = True; return True
    def close(self): self.connected = False
    async def read_input_registers(self, *, address, count, device_id=1):
        self.calls.append((address, count, device_id)); return Response()
    async def read_holding_registers(self, *, address, count, device_id=1): return Response()
    async def write_register(self, *, address, value, device_id=1):
        self.calls.append((address, value, device_id)); return Response()
client.AsyncModbusSerialClient = FakeClient; client.AsyncModbusTcpClient = FakeClient
sys.modules.update({'pymodbus': pm, 'pymodbus.client': client, 'pymodbus.exceptions': errors})
spec = importlib.util.spec_from_file_location('fake.hub', root/'hub.py')
mod = importlib.util.module_from_spec(spec); sys.modules['fake.hub'] = mod; spec.loader.exec_module(mod)
class Entry:
    options = {}
    def __init__(self, data): self.data = data
async def main():
    tcp = mod.SandiSolarModbusHub(None, Entry({'transport':'tcp', 'host':'192.168.1.50', 'tcp_port':8899, 'slave':7}))
    c = tcp._create_client(); assert c.kw['host']=='192.168.1.50' and c.kw['port']==8899
    assert 'baudrate' not in c.kw
    await tcp.async_init(); tcp._last_request_time = 0
    assert await tcp.read_input_register('grid_voltage') == 230.0
    assert tcp._client.calls[-1] == (42, 1, 7)
    assert await tcp.write_holding_register('sec_eps_on_vbat', 45) is False
    await tcp.close()
    serial = mod.SandiSolarModbusHub(None, Entry({'port':'/dev/ttyUSB0','baudrate':9600,'slave':1}))
    assert serial._create_client().kw['port']=='/dev/ttyUSB0'
    assert serial.transport=='serial'
    print('TCP host/port, Modbus ID, register read, blocked write and legacy serial entry: OK')
asyncio.run(main())

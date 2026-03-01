from langchain_core.tools import tool

@tool("booking_appointment", description="Agendar una cita médica en una fecha y hora en específico, para un paciente y un doctor específicos")
def booking_appointment(fecha: str, tiempo: str, doctor: str, paciente: str) -> str:
    # lógica real: validar, reservar y manejar errores
    return (
        f"Cita confirmada: paciente {paciente}, doctor {doctor}, "
        f"fecha {fecha}, hora {tiempo}."
    )

@tool("get_appointment_availability", description="Verificar disponibilidad de citas")
def get_appointment_availability(fecha: str, tiempo: str, doctor: str) -> str:
    # lógica real: consultar agenda y formatear 'slots' útiles
    return (
        f"Disponibilidad para {doctor} en {fecha} {tiempo}: 14:00, 15:00, 16:00. "
        "Indica tu hora preferida."
    )

tools = [booking_appointment, get_appointment_availability]
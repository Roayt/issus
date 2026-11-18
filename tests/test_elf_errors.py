from issus.elf_error import ElfError


def test_failed_to_Parse():
    failed_to_parse_value=ElfError.FailedToParse
    assert failed_to_parse_value==1

def test_invalid_program_Header():
    invalid_program_header_value=ElfError.InvalidProgramHeader
    assert invalid_program_header_value==23

def test_value_out_0f_bounds():
    value_out_of_bounds_value=ElfError.ValueOutOfBounds

    assert value_out_of_bounds_value==21

def test_unsupported_sbpf_version():
    unsupported_sbpf_versionvalue=ElfError.UnsupportedSBPFVersion
    assert unsupported_sbpf_versionvalue ==22

def test_total_error_code():
    total_error_code=len(ElfError)

    assert total_error_code ==23
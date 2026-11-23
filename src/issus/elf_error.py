from enum import IntEnum


class ElfError(IntEnum):
    FailedToParse = 1
    EntrypointOutOfBounds = 2
    InvalidEntrypoint = 3
    FailedToGetSection = 4
    UnresolvedSymbol = 5
    SectionNotFound = 6
    RelativeJumpOutOfBounds = 7
    SymbolHashCollision = 8
    WrongEndianess = 9
    WrongAbi = 10
    WrongMachine = 11
    WrongClass = 12
    NotOneTextSection = 13
    WritableSectionNotSupported = 14
    AddressOutsideLoadableSection = 15
    InvalidVirtualAddress = 16
    UnknownRelocation = 17
    FailedToReadRelocationInfo = 18
    WrongType = 19
    UnknownSymbol = 20
    ValueOutOfBounds = 21
    UnsupportedSBPFVersion = 22
    InvalidProgramHeader = 23

from enum import Enum


class FilingType(Enum):
    """Available filing types to be used when creating Filing object.

    .. versionadded:: 0.1.5
    """

    FILING_1 = '1'
    FILING_1A = '1-a'
    FILING_1E = '1-e'
    FILING_1K = '1-k'
    FILING_1N = '1-n'
    FILING_1SA = '1-sa'
    FILING_1U = '1-u'
    FILING_1Z = '1-z'
    FILING_10 = '10'
    FILING_10D = '10-d'
    FILING_10K = '10-k'
    FILING_10M = '10-m'
    FILING_10Q = '10-q'
    FILING_11K = '11-k'
    FILING_12B25 = '12b-25'
    FILING_13F = '13f'
    FILING_13H = '13h'
    FILING_144 = '144'
    FILING_15 = '15'
    FILING_15F = '15f'
    FILING_17H = '17-h'
    FILING_18 = '18'
    FILING_18K = '18-k'
    FILING_19B4 = '19b-4'
    FILING_19B4E = '19b-4(e)'
    FILING_19B7 = '19b-7'
    FILING_2E = '2-e'
    FILING_20F = '20-f'
    FILING_24F2 = '24f-2'
    FILING_25 = '25'
    FILING_3 = '3'
    FILING_4 = '4'
    FILING_40F = '40-f'
    FILING_8K = '8-k'
    FILING_ABS15G = 'abs-15g'
    FILING_ABSEE = 'abs-ee'
    FILING_ADV = 'adv'
    FILING_ADVE = 'adv-e'
    FILING_ADVH = 'adv-h'
    FILING_ADVNR = 'adv-nr'
    FILING_ADVW = 'adv-w'
    FILING_ATS = 'ats'
    FILING_ATSN = 'ats-n'
    FILING_ATSR = 'ats-r'
    FILING_BD = 'bd'
    FILING_BDN = 'bd-n'
    FILING_BDW = 'bdw'
    FILING_C = 'c'
    FILING_CA1 = 'ca-1'
    FILING_CB = 'cb'
    FILING_CFPORTAL = 'cfportal'
    FILING_CUSTODY = 'custody'
    FILING_D = 'd'
    FILING_F1 = 'f-1'
    FILING_F10 = 'f-10'
    FILING_F3 = 'f-3'
    FILING_F4 = 'f-4'
    FILING_F6 = 'f-6'
    FILING_F7 = 'f-7'
    FILING_F8 = 'f-8'
    FILING_F80 = 'f-80'
    FILING_FN = 'f-n'
    FILING_FX = 'f-x'
    FILING_ID = 'id'
    FILING_MA = 'ma'
    FILING_MAI = 'ma-i'
    FILING_MANR = 'ma-nr'
    FILING_MAW = 'ma-w'
    FILING_MSD = 'msd'
    FILING_MSDW = 'msdw'
    FILING_N14 = 'n-14'
    FILING_N17D1 = 'n-17d-1'
    FILING_N17F1 = 'n-17f-1'
    FILING_N17F2 = 'n-17f-2'
    FILING_N18F1 = 'n-18f-1'
    FILING_N1A = 'n-1a'
    FILING_N2 = 'n-2'
    FILING_N23C3 = 'n-23c-3'
    FILING_N27D1 = 'n27d-1'
    FILING_N3 = 'n-3'
    FILING_N4 = 'n-4'
    FILING_N5 = 'n-5'
    FILING_N54A = 'n-54a'
    FILING_N54C = 'n-54c'
    FILING_N6 = 'n-6'
    FILING_N6EI1 = 'n-6ei-1'
    FILING_N6F = 'n-6f'
    FILING_N8A = 'n-8a'
    FILING_N8B2 = 'n-8b-2'
    FILING_N8B4 = 'n-8b-4'
    FILING_N8F = 'n-8f'
    FILING_NCEN = 'n-cen'
    FILING_NCR = 'n-cr'
    FILING_NCSR = 'n-csr'
    FILING_NCSRS = 'n-csrs'
    FILING_NLIQUID = 'n-liquid'
    FILING_NMFP = 'n-mfp'
    FILING_NPORT = 'n-port'
    FILING_NPX = 'n-px'
    FILING_NQ = 'n-q'
    FILING_NRSRO = 'nrsro'
    FILING_PF = 'pf'
    FILING_PILOT = 'pilot'
    FILING_R31 = 'r31'
    FILING_S1 = 's-1'
    FILING_S11 = 's-11'
    FILING_S20 = 's-20'
    FILING_S3 = 's-3'
    FILING_S4 = 's-4'
    FILING_S6 = 's-6'
    FILING_S8 = 's-8'
    FILING_SBSE = 'sbse'
    FILING_SBSEA = 'sbse-a'
    FILING_SBSEBD = 'sbse-bd'
    FILING_SBSEC = 'sbse-c'
    FILING_SBSEW = 'sbse-w'
    FILING_SCI = 'sci'
    FILING_SD = 'sd'
    FILING_SDR = 'sdr'
    FILING_SE = 'se'
    FILING_SF1 = 'sf-1'
    FILING_SF3 = 'sf-3'
    FILING_SIP = 'sip'
    FILING_T1 = 't-1'
    FILING_T2 = 't-2'
    FILING_T3 = 't-3'
    FILING_T4 = 't-4'
    FILING_T6 = 't-6'
    FILING_TA1 = 'ta-1'
    FILING_TA2 = 'ta-2'
    FILING_TAW = 'ta-w'
    FILING_TCR = 'tcr'
    FILING_TH = 'th'
    FILING_WBAPP = 'wb-app'

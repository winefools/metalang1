# natural_parser.py
from mapping_table import find_mapping, generate_dsl_command, extract_parameters

def natural_to_metalang(text):
    """자연어 문장을 메타랭 명령어 문자열로 변환"""
    
    # 매핑 테이블에서 적합한 매핑 찾기
    mapping_name, mapping_data = find_mapping(text)
    
    if mapping_name and mapping_data:
        # 파라미터 추출
        extracted_params = extract_parameters(text, mapping_name)
        
        # DSL 명령어 생성
        dsl_command = generate_dsl_command(text, mapping_data, extracted_params)
        return dsl_command
    
    # 매핑을 찾지 못한 경우 기본 처리
    return f'[T900: unknown, "{text}"]'

def natural_to_metalang_with_gpt(text):
    """GPT를 사용한 고급 자연어 처리 (기존 기능 유지)"""
    
    # 먼저 매핑 테이블로 시도
    mapping_name, mapping_data = find_mapping(text)
    
    if mapping_name and mapping_data:
        extracted_params = extract_parameters(text, mapping_name)
        dsl_command = generate_dsl_command(text, mapping_data, extracted_params)
        return dsl_command
    
    # 매핑 테이블에서 찾지 못한 경우 GPT 사용
    from gpt_wrapper import gpt_expand_command
    return gpt_expand_command(text)

